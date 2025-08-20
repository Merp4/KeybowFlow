"""
KeybowFlow - Main runtime
Implements key press and release handling to avoid stuck keys.
"""

import time
import usb_hid
from pmk import PMK
from pmk.platform.keybow2040 import Keybow2040 as Hardware

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl

# Import configuration and constants
try:
    from keymap import LAYERS, COLORS, CONFIG
    print("[INFO] Configuration loaded from keymap.py")
except Exception as e:
    print(f"[ERROR] Failed to import configuration from keymap.py: {e}")
    raise

from constants import ActionType, Color, LayerAction


def _safe_has_debug_flag():
    try:
        return bool(CONFIG.get("debug", False))
    except Exception:
        return False


DEBUG = _safe_has_debug_flag()


def log_debug(*args):
    if DEBUG:
        print("[DEBUG]", *args)


def log_info(*args):
    print("[INFO]", *args)


def log_error(*args):
    print("[ERROR]", *args)


class KeybowController:
    def __init__(self):
        self._initialize_hardware()
        self._initialize_hid_devices()
        self._load_configuration()
        self._setup_led_settings()
        self._setup_key_handlers()
        self._apply_initial_layer()

        self.pressed_keys = set()
        self.held_keys = set()
        self.pressed_actions = {}  # key_num -> int or list that was pressed

        for key in self.keys:
            key.is_pressed = False

        log_info("Keybow initialized successfully!")
        log_info(f"Config: {CONFIG.get('name', 'Unnamed')} v{CONFIG.get('version', 'None')}")
        layer_name = LAYERS.get(self.current_layer, {}).get('name', f"Layer {self.current_layer}")
        log_info(f"Starting layer: {self.current_layer} ({layer_name})")

    def _initialize_hardware(self):
        try:
            import gc
            gc.collect()
            self.keybow = PMK(Hardware())
            self.keys = self.keybow.keys
            log_info("Hardware initialized")
        except Exception as e:
            log_error(f"Failed to initialize hardware: {e}")
            raise

    def _initialize_hid_devices(self):
        try:
            self.keyboard = Keyboard(usb_hid.devices)
            self.layout = KeyboardLayoutUS(self.keyboard)
            self.consumer_control = ConsumerControl(usb_hid.devices)
            log_info("HID devices initialized")
        except Exception as e:
            log_error(f"Failed to initialize HID devices: {e}")
            raise

    def _load_configuration(self):
        self.layers = LAYERS
        self.colors = COLORS
        if not self.layers:
            raise ValueError("No layers defined in configuration")
        self.current_layer = CONFIG.get('default_layer', 0)
        if self.current_layer not in self.layers:
            raise ValueError(f"Default layer {self.current_layer} not found in LAYERS")
        self.held_modifiers = set()
        log_info("Configuration loaded and validated")

    def _setup_led_settings(self):
        self.keybow.led_sleep_enabled = CONFIG.get('led_sleep_enabled', True)
        self.keybow.led_sleep_time = CONFIG.get('led_sleep_time', 30)
        self.brightness = CONFIG.get('brightness', 1.0)
        log_info(f"LED settings: sleep={self.keybow.led_sleep_enabled}, brightness={self.brightness}")

    def _setup_key_handlers(self):
        for key in self.keys:
            self._attach_key_handlers(key)

    def _attach_key_handlers(self, key):
        @self.keybow.on_press(key)
        def press_handler(_, k=key):
            self.handle_key_press(k)

        @self.keybow.on_release(key)
        def release_handler(_, k=key):
            self.handle_key_release(k)

        @self.keybow.on_hold(key)
        def hold_handler(_, k=key):
            self.handle_key_hold(k)

    def _apply_initial_layer(self):
        self.update_layer_colors()

    def get_color_rgb(self, color_input):
        if isinstance(color_input, (tuple, list)) and len(color_input) == 3:
            return tuple(int(c * self.brightness) for c in color_input)
        if isinstance(color_input, str) and color_input in self.colors:
            color = self.colors[color_input]
            return tuple(int(c * self.brightness) for c in color)
        off_color = self.colors.get('off', (0, 0, 0))
        return tuple(int(c * self.brightness) for c in off_color)

    def get_key_config(self, key_num, layer=None):
        layer = self.current_layer if layer is None else layer
        return self.layers.get(layer, {}).get('keys', {}).get(key_num)

    def update_layer_colors(self):
        name = self.layers[self.current_layer]['name']
        log_info(f"Updating colors for layer: {name}")
        for key in self.keys:
            cfg = self.get_key_config(key.number)
            if cfg and 'colors' in cfg:
                default_color = cfg['colors'].get('default', 'off')
                key.set_led(*self.get_color_rgb(default_color))
            else:
                key.led_off()

    def handle_key_press(self, key):
        key_num = key.number
        config = self.get_key_config(key_num)
        log_info(f"handle_key_press: key {key_num} pressed, config: {config}")

        if config and 'colors' in config:
            pressed_color = config['colors'].get('pressed', 'white')
            key.set_led(*self.get_color_rgb(pressed_color))

        if not config:
            return

        # Modifier key
        if (
            (isinstance(config, dict) and config.get('action_type') == 'modifier')
            or (isinstance(config, dict) and isinstance(config.get('action'), dict) and config['action'].get('action_type') == 'modifier')
        ):
            self.held_modifiers.add(key_num)
            log_info(f"Modifier key pressed (key {key_num}) - layer switching enabled")
            return

        # Dual-action selection
        if isinstance(config, dict) and ('default' in config and 'modifier' in config):
            chosen = config['modifier'] if len(self.held_modifiers) > 0 else config['default']
            if isinstance(chosen, dict) and chosen.get('action_type') == ActionType.LAYER:
                self.switch_layer(chosen.get('action'))
                return
            if isinstance(chosen, (int, list)):
                self._execute_key_action(chosen, press_only=True)
                self.pressed_keys.add(key_num)
                self.pressed_actions[key_num] = chosen
                return
            if isinstance(chosen, dict):
                at = chosen.get('action_type')
                if at == ActionType.KEY:
                    act = chosen.get('action')
                    self._execute_key_action(act, press_only=True)
                    self.pressed_keys.add(key_num)
                    self.pressed_actions[key_num] = act
                    return
                else:
                    self.execute_action(chosen, key, press_only=False)
                    return

        # Plain action
        at = config.get('action_type', ActionType.NONE)
        if at == ActionType.KEY:
            act = config.get('action')
            self._execute_key_action(act, press_only=True)
            self.pressed_keys.add(key_num)
            self.pressed_actions[key_num] = act
        elif at == ActionType.LAYER:
            self._handle_layer_switching(config)
        else:
            self.execute_action(config, key, press_only=False)

    def _handle_layer_switching(self, config):
        if config.get('action_type') != ActionType.LAYER:
            return False
        action = config.get('action')
        if action == LayerAction.MODIFIER:
            return False
        if isinstance(action, int) and action in self.layers:
            self.switch_layer(action)
            return True
        return False

    def handle_key_release(self, key):
        key_num = key.number
        config = self.get_key_config(key_num)
        log_info(f"handle_key_release: key {key_num} released, config: {config}")

        if config and (
            (isinstance(config, dict) and config.get('action_type') == 'modifier')
            or (isinstance(config, dict) and isinstance(config.get('action'), dict) and config['action'].get('action_type') == 'modifier')
        ):
            if key_num in self.held_modifiers:
                self.held_modifiers.remove(key_num)
                log_info(f"Modifier key released (key {key_num})")

        if key_num in self.pressed_keys:
            self.pressed_keys.remove(key_num)
            pressed_action = self.pressed_actions.pop(key_num, None)
            if pressed_action is not None:
                self._release_key_action(pressed_action)

        if config and 'colors' in config:
            default_color = config['colors'].get('default', 'off')
            key.set_led(*self.get_color_rgb(default_color))
        else:
            key.led_off()

    def handle_key_hold(self, key):
        key_num = key.number
        config = self.get_key_config(key_num)
        log_info(f"handle_key_hold: key {key_num} held, config: {config}")
        if config and 'colors' in config:
            held_color = config['colors'].get('held', 'yellow')
            key.set_led(*self.get_color_rgb(held_color))
        self.held_keys.add(key_num)

    def switch_layer(self, new_layer):
        if new_layer not in self.layers:
            log_error(f"Invalid layer: {new_layer}")
            return
        old_layer = self.current_layer
        self.current_layer = new_layer
        self.update_layer_colors()
        old_name = LAYERS.get(old_layer, {}).get('name', f"Layer {old_layer}")
        new_name = LAYERS.get(new_layer, {}).get('name', f"Layer {new_layer}")
        log_info(f"Layer switch: {old_name} -> {new_name}")

    def execute_action(self, config, key=None, press_only=False):
        at = config.get('action_type', ActionType.NONE)
        action = config.get('action')
        if at == ActionType.NONE or action is None:
            return
        try:
            if at == ActionType.KEY:
                self._execute_key_action(action, press_only)
            elif at == ActionType.SEQUENCE and not press_only:
                self._execute_sequence_action(action)
            elif at == ActionType.STRING and not press_only:
                self._execute_string_action(action)
            elif at == ActionType.CONSUMER and not press_only:
                self._execute_consumer_action(action)
            elif at == ActionType.FUNCTION and not press_only:
                self._execute_function_action(action, key)
        except Exception as e:
            log_error(f"Error executing {at} action: {e}")

    def release_action(self, config, key=None):
        at = config.get('action_type', ActionType.NONE)
        action = config.get('action')
        if at == ActionType.KEY and action is not None:
            try:
                self._release_key_action(action)
            except Exception as e:
                log_error(f"Error releasing {at} action: {e}")

    def _execute_key_action(self, action, press_only=False):
        if action is None:
            return
        if isinstance(action, list):
            if press_only:
                self.keyboard.press(*action)
                log_info(f"Key combination pressed: {[str(k) for k in action]}")
            else:
                self.keyboard.send(*action)
                log_info(f"Key combination: {[str(k) for k in action]}")
        elif isinstance(action, int):
            if press_only:
                self.keyboard.press(action)
                log_info(f"Key pressed: {action} (value: {action})")
            else:
                self.keyboard.send(action)
                log_info(f"Key: {action} (value: {action})")

    def _release_key_action(self, action):
        action_val = self._extract_action(action)
        if action_val is None:
            return
        if isinstance(action_val, list):
            self.keyboard.release(*action_val)
            log_info(f"Key combination released: {[str(k) for k in action_val]}")
        elif isinstance(action_val, int):
            self.keyboard.release(action_val)
            log_info(f"Key released: {action_val} (value: {action_val})")

    def _execute_sequence_action(self, action):
        log_info(f"Sequence: {action}")
        for item in action:
            if isinstance(item, list):
                self.keyboard.send(*item)
            else:
                self.keyboard.send(item)
            time.sleep(0.01)

    def _execute_string_action(self, action):
        try:
            self.layout.write(action)
            log_info(f"Typed: '{action}'")
        except Exception as e:
            log_error(f"Failed to type string action: {e}")

    def _execute_consumer_action(self, action):
        try:
            self.consumer_control.send(action)
            log_info(f"Media: {action}")
        except Exception as e:
            log_error(f"Failed to send consumer action: {e}")

    def _execute_function_action(self, action, key=None):
        if action == 'toggle_all_leds':
            self._toggle_all_leds()
        elif action == 'show_layer_info':
            self._show_layer_info()
        elif action == 'brightness_up':
            self._adjust_brightness(0.1)
        elif action == 'brightness_down':
            self._adjust_brightness(-0.1)
        else:
            log_error(f"Unknown function: {action}")

    def _toggle_all_leds(self):
        for key in self.keys:
            key.toggle_led()
        log_info("Toggled all LEDs")

    def _show_layer_info(self):
        layer_info = self.layers[self.current_layer]
        key_count = len(layer_info.get('keys', {}))
        log_info("Layer {idx}: {name} ({count} keys configured)".format(
            idx=self.current_layer,
            name=LAYERS.get(self.current_layer, {}).get('name', f"Layer {self.current_layer}"),
            count=key_count,
        ))

    def _adjust_brightness(self, delta):
        try:
            current = getattr(self, 'brightness', 1.0) or 1.0
            self.brightness = max(0.1, min(1.0, current + delta))
            log_info("Brightness: {:.1f}".format(self.brightness))
            self.update_layer_colors()
        except Exception as e:
            log_error(f"Failed to adjust brightness: {e}")

    def release_all_keys(self):
        try:
            self.keyboard.release_all()
            log_info("Released all pressed keys")
            for key in self.keys:
                key.led_off()
            log_info("All LEDs turned off")
            self.pressed_keys.clear()
            self.held_keys.clear()
            self.pressed_actions.clear()
        except Exception as e:
            log_error(f"Error during cleanup: {e}")

    def run(self):
        log_info("\n" + "=" * 50)
        log_info("Keybow Controller Starting")
        log_info("=" * 50)
        layer_name = LAYERS.get(self.current_layer, {}).get('name', f"Layer {self.current_layer}")
        log_info(f"Current layer: {self.current_layer} ({layer_name})")
        log_info("Press Ctrl+C to stop")
        log_info("=" * 50 + "\n")
        try:
            while True:
                self.keybow.update()
        except KeyboardInterrupt:
            log_info("Keybow Controller stopped by user")
            self.release_all_keys()
        except Exception as e:
            log_error(f"Unexpected error: {e}")
            self.release_all_keys()
            log_info("Restarting in 3 seconds...")
            time.sleep(3)
            self.run()

    def _extract_action(self, config):
        if config is None:
            return None
        if isinstance(config, dict):
            if 'modifier' in config and 'default' in config:
                if len(self.held_modifiers) > 0:
                    return self._extract_action(config['modifier'])
                return self._extract_action(config['default'])
            if 'action' in config:
                return self._extract_action(config['action'])
        if isinstance(config, (int, list)):
            return config
        return None


def main():
    controller = KeybowController()
    controller.run()


if __name__ == "__main__":
    main()

