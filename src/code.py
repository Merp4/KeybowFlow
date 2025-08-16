# KeybowFlow - Main Runtime
# Professional workflow automation for Keybow 2040
# 
# Configuration is loaded from keymap.py for easy customization.
# Supports multiple layers, various action types, and customizable LED colors.
#
# Action Types Supported:
# - KEY: Single keycode or key combination (e.g., Keycode.A or [Keycode.CTRL, Keycode.C])
# - SEQUENCE: Sequence of keys/combinations (e.g., [Keycode.A, [Keycode.CTRL, Keycode.C]])
# - STRING: Type text strings
# - CONSUMER: Media/consumer controls
# - LAYER: Switch to different layer
# - FUNCTION: Custom functions (extensible)
# - NONE: No action

import time
import usb_hid
from pmk import PMK
from pmk.platform.keybow2040 import Keybow2040 as Hardware

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl

# Lightweight CircuitPython-friendly logging helpers
def _safe_has_debug_flag():
    try:
        # CONFIG may not be defined yet; calling this is safe because exceptions are caught
        return bool(CONFIG.get('debug', False))
    except Exception:
        return False

DEBUG = _safe_has_debug_flag()

def log_debug(*args, **kwargs):
    if DEBUG:
        print("[DEBUG]", *args, **kwargs)

def log_info(*args, **kwargs):
    print("[INFO]", *args, **kwargs)

def log_error(*args, **kwargs):
    print("[ERROR]", *args, **kwargs)

# Import our configuration and constants
try:
    from keymap import LAYERS, COLORS, CONFIG, get_layer_name, get_config_info
    log_info("Configuration loaded from keymap.py")
except ImportError as e:
    log_error(f"Failed to import configuration from keymap.py: {e}")
    log_info("Please copy a configuration from examples/configs/ to keymap.py")
    log_info("   Example: copy examples\\configs\\numpad_minimal.py src\\keymap.py")
    raise ImportError("No configuration found in keymap.py. Please copy an example configuration.")

from constants import ActionType, Key, Color, LayerAction

# =====================================================================================
# MAIN CONTROLLER CLASS
# =====================================================================================

class KeybowController:
    """
    Main controller class for the Keybow 2040.
    Handles key events, layer switching, and action execution.
    """
    
    def __init__(self):
        """Initialize the Keybow controller with hardware and configuration.

        This sets up hardware, HID devices, configuration, LED settings,
        key handlers, and applies the initial layer. It also initializes
        runtime tracking structures and prints a short startup summary.
        """
        # Initialize subsystems
        self._initialize_hardware()
        self._initialize_hid_devices()
        self._load_configuration()
        self._setup_led_settings()
        self._setup_key_handlers()
        self._apply_initial_layer()

        # Track pressed and held keys for release handling
        self.pressed_keys = set()
        self.held_keys = set()

        # Display configuration info
        config_info = get_config_info()
        log_info("Keybow initialized successfully!")
        log_info(f"Config: {config_info.get('name')} v{config_info.get('version')}")
        log_info(f"Starting layer: {self.current_layer} ({get_layer_name(self.current_layer)})")
        log_info(f"Available layers: {', '.join(config_info.get('layers', {}).values())}")

    def _initialize_hardware(self):
        """Initialize the PMK hardware."""
        try:
            # First, try to clean up any existing hardware instances
            import gc
            gc.collect()
            
            self.keybow = PMK(Hardware())
            self.keys = self.keybow.keys
            log_info("Hardware initialized")
        except Exception as e:
            log_error(f"Failed to initialize hardware: {e}")
            if "in use" in str(e):
                log_info("Hardware may be in use by another process. Disconnect and reconnect the device.")
                # Try to reset and reinitialize
                try:
                    import supervisor
                    log_info("Attempting to reload supervisor...")
                    supervisor.reload()
                except:
                    pass
            raise

    def _initialize_hid_devices(self):
        """Initialize HID devices for keyboard and consumer control."""
        try:
            self.keyboard = Keyboard(usb_hid.devices)
            self.layout = KeyboardLayoutUS(self.keyboard)
            self.consumer_control = ConsumerControl(usb_hid.devices)
            log_info("HID devices initialized")
        except Exception as e:
            log_error(f"Failed to initialize HID devices: {e}")
            raise

    def _load_configuration(self):
        """Load and validate configuration settings."""
        self.layers = LAYERS
        self.colors = COLORS
        
        # Validate configuration
        if not self.layers:
            raise ValueError("No layers defined in configuration")
        
        self.current_layer = CONFIG['default_layer']
        self.modifier_key_num = CONFIG.get('modifier_key')
        
        if self.current_layer not in self.layers:
            raise ValueError(f"Default layer {self.current_layer} not found in LAYERS")

        self.modifier_held = False
        log_info("Configuration loaded and validated")

    def _setup_led_settings(self):
        """Configure LED sleep and brightness settings."""
        self.keybow.led_sleep_enabled = CONFIG.get('led_sleep_enabled', True)
        self.keybow.led_sleep_time = CONFIG.get('led_sleep_time', 30)
        self.brightness = CONFIG.get('brightness', 1.0)

        # Log LED settings
        log_info(
            "LED settings: sleep={sleep}, brightness={brightness}".format(
                sleep=self.keybow.led_sleep_enabled, brightness=self.brightness
            )
        )

    def _setup_key_handlers(self):
        """Setup event handlers for all keys with proper closure handling."""
        for key in self.keys:
            # Use default parameter to capture the key in closure
            self._attach_key_handlers(key)

    def _attach_key_handlers(self, key):
        """Attach event handlers to a specific key."""
        @self.keybow.on_press(key)
        def press_handler(pressed_key, k=key):
            self.handle_key_press(k)
        
        @self.keybow.on_release(key)
        def release_handler(released_key, k=key):
            self.handle_key_release(k)
            
        @self.keybow.on_hold(key)
        def hold_handler(held_key, k=key):
            self.handle_key_hold(k)

    def _apply_initial_layer(self):
        """Apply the initial layer colors and settings."""
        self.update_layer_colors()

    def get_color_rgb(self, color_input):
        """
        Convert color name or RGB tuple to RGB tuple with brightness adjustment.
        
        Args:
            color_input: Either a color name (str) from COLORS dict, or an RGB tuple
            
        Returns:
            tuple: RGB tuple (r, g, b) with brightness applied
        """
        # If it's already an RGB tuple, apply brightness directly
        if isinstance(color_input, (tuple, list)) and len(color_input) == 3:
            return tuple(int(c * self.brightness) for c in color_input)
        
        # If it's a color name, look it up in the COLORS dictionary
        if isinstance(color_input, str) and color_input in self.colors:
            color = self.colors[color_input]
            return tuple(int(c * self.brightness) for c in color)
        
        # Fallback to 'off' color if not found
        off_color = self.colors.get('off', (0, 0, 0))
        return tuple(int(c * self.brightness) for c in off_color)

    def get_key_config(self, key_num, layer=None):
        """
        Get configuration for a specific key in the current or specified layer.
        
        Args:
            key_num (int): Key number (0-15)
            layer (int, optional): Layer number. Defaults to current layer.
            
        Returns:
            dict or None: Key configuration or None if not found
        """
        if layer is None:
            layer = self.current_layer
        
        return self.layers.get(layer, {}).get('keys', {}).get(key_num)

    def update_layer_colors(self):
        """Update all key colors for the current layer."""
        layer_name = self.layers[self.current_layer]['name']
        log_info(f"Updating colors for layer: {layer_name}")

        for key in self.keys:
            config = self.get_key_config(key.number)
            if config and 'colors' in config:
                default_color = config['colors'].get('default', 'off')
                color_rgb = self.get_color_rgb(default_color)
                key.set_led(*color_rgb)
            else:
                key.led_off()

    def handle_key_press(self, key):
        """
        Handle key press events.
        
        Args:
            key: PMK key object
        """
        key_num = key.number
        config = self.get_key_config(key_num)
        
        # Update LED color for press
        if config and 'colors' in config:
            pressed_color = config['colors'].get('pressed', 'white')
            color_rgb = self.get_color_rgb(pressed_color)
            key.set_led(*color_rgb)

        # Handle modifier key
        if self.modifier_key_num is not None and key_num == self.modifier_key_num:
            self.modifier_held = True
            log_info("Modifier key pressed - layer switching enabled")
            return
        
        # Handle layer switching
        if self.modifier_held and config:
            if self._handle_layer_switching(config):
                return
        
        # Track pressed key
        self.pressed_keys.add(key_num)
        
        # Execute regular key action with press_only for KEY actions
        if config:
            action_type = config.get('action_type', ActionType.NONE)
            if action_type == ActionType.KEY:
                # For KEY actions, press and hold until release
                self.execute_action(config, key, press_only=True)
            else:
                # For other actions, execute immediately (strings, consumer, etc.)
                self.execute_action(config, key, press_only=False)

    def _handle_layer_switching(self, config):
        """
        Handle layer switching logic.
        
        Args:
            config (dict): Key configuration
            
        Returns:
            bool: True if layer switch was handled, False otherwise
        """
        if config.get('action_type') == ActionType.LAYER:
            action = config.get('action')
            
            if action == LayerAction.MODIFIER:
                # This is the modifier key itself
                return False
            elif isinstance(action, int) and action in self.layers:
                self.switch_layer(action)
                return True
        
        return False

    def handle_key_release(self, key):
        """
        Handle key release events.
        
        Args:
            key: PMK key object
        """
        key_num = key.number
        config = self.get_key_config(key_num)
        
        # Handle modifier key release
        if self.modifier_key_num is not None and key_num == self.modifier_key_num:
            self.modifier_held = False
            log_info("Modifier key released")
        
        # Release any pressed keys for this key
        if key_num in self.pressed_keys:
            self.pressed_keys.remove(key_num)
            # Release the key action if it was a KEY type
            if config:
                action_type = config.get('action_type', ActionType.NONE)
                if action_type == ActionType.KEY:
                    self.release_action(config, key)
        
        # Remove from held keys if it was held
        if key_num in self.held_keys:
            self.held_keys.remove(key_num)
        
        # Restore default LED color
        if config and 'colors' in config:
            default_color = config['colors'].get('default', 'off')
            color_rgb = self.get_color_rgb(default_color)
            key.set_led(*color_rgb)
        else:
            key.led_off()

    def handle_key_hold(self, key):
        """
        Handle key hold events.
        
        Args:
            key: PMK key object
        """
        key_num = key.number
        config = self.get_key_config(key_num)
        
        # Update LED color for hold
        if config and 'colors' in config:
            held_color = config['colors'].get('held', 'yellow')
            color_rgb = self.get_color_rgb(held_color)
            key.set_led(*color_rgb)
            # Track held key
            self.held_keys.add(key_num)

            log_debug(f"Key {key_num} held")

            # Maintain pressed key behavior during hold
            # Key release will handle cleanup

    def switch_layer(self, new_layer):
        """
        Switch to a new layer.
        
        Args:
            new_layer (int): Target layer number
        """
        if new_layer not in self.layers:
            log_error(f"Invalid layer: {new_layer}")
            return

        old_layer = self.current_layer
        self.current_layer = new_layer
        self.update_layer_colors()

        old_name = get_layer_name(old_layer)
        new_name = get_layer_name(new_layer)
        log_info(f"Layer switch: {old_name} -> {new_name}")

    def execute_action(self, config, key=None, press_only=False):
        """
        Execute the action defined in the key configuration.
        
        Args:
            config (dict): Key configuration
            key: PMK key object (optional)
            press_only (bool): If True, only press keys without releasing them
        """
        action_type = config.get('action_type', ActionType.NONE)
        action = config.get('action')
        
        if action_type == ActionType.NONE or action is None:
            return
        
        try:
            if action_type == ActionType.KEY:
                self._execute_key_action(action, press_only)
            elif action_type == ActionType.SEQUENCE:
                if not press_only:  # Sequences don't support press_only mode
                    self._execute_sequence_action(action)
            elif action_type == ActionType.STRING:
                if not press_only:  # Strings don't support press_only mode
                    self._execute_string_action(action)
            elif action_type == ActionType.CONSUMER:
                if not press_only:  # Consumer controls don't support press_only mode
                    self._execute_consumer_action(action)
            elif action_type == ActionType.FUNCTION:
                if not press_only:  # Functions don't support press_only mode
                    self._execute_function_action(action, key)
            elif action_type == ActionType.LAYER:
                # Layer switching is handled in handle_key_press
                pass
            else:
                log_error(f"Unknown action type: {action_type}")
                
        except Exception as e:
            log_error(f"Error executing {action_type} action: {e}")

    def release_action(self, config, key=None):
        """
        Release the action defined in the key configuration.
        
        Args:
            config (dict): Key configuration  
            key: PMK key object (optional)
        """
        action_type = config.get('action_type', ActionType.NONE)
        action = config.get('action')
        
        if action_type == ActionType.NONE or action is None:
            return
        
        try:
            if action_type == ActionType.KEY:
                self._release_key_action(action)
            # Other action types don't need explicit release
                
        except Exception as e:
            log_error(f"Error releasing {action_type} action: {e}")

    def _execute_key_action(self, action, press_only=False):
        """Execute a key or key combination action."""
        if isinstance(action, list):
            # Key combination (e.g., Ctrl+C)
            if press_only:
                self.keyboard.press(*action)
                log_info(f"Key combination pressed: {[str(k) for k in action]}")
            else:
                self.keyboard.send(*action)  # Press and release
                log_info(f"Key combination: {[str(k) for k in action]}")
        else:
            # Single keycode
            if press_only:
                self.keyboard.press(action)
                log_info(f"Key pressed: {action} (value: {action})")
            else:
                self.keyboard.send(action)  # Press and release
                log_info(f"Key: {action} (value: {action})")

    def _release_key_action(self, action):
        """Release a key or key combination action."""
        if isinstance(action, list):
            # Key combination (e.g., Ctrl+C)
            self.keyboard.release(*action)
            log_info(f"Key combination released: {[str(k) for k in action]}")
        else:
            # Single keycode
            self.keyboard.release(action)
            log_info(f"Key released: {action} (value: {action})")

    def _execute_sequence_action(self, action):
        """Execute a sequence of keys/combinations."""
        log_info(f"Sequence: {action}")
        for item in action:
            if isinstance(item, list):
                self.keyboard.send(*item)
            else:
                self.keyboard.send(item)
            time.sleep(0.01)  # Small delay between actions

    def _execute_string_action(self, action):
        """Execute a string typing action."""
        # Use the layout to type the provided string
        try:
            self.layout.write(action)
            log_info(f"Typed: '{action}'")
        except Exception as e:
            log_error(f"Failed to type string action: {e}")

    def _execute_consumer_action(self, action):
        """Execute a consumer/media control action."""
        try:
            self.consumer_control.send(action)
            log_info(f"Media: {action}")
        except Exception as e:
            log_error(f"Failed to send consumer action: {e}")

    def _execute_function_action(self, action, key=None):
        """Execute a custom function action."""
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
        """Toggle all LED states."""
        for key in self.keys:
            key.toggle_led()
        log_info("Toggled all LEDs")

    def _show_layer_info(self):
        """Display current layer information."""
        layer_info = self.layers[self.current_layer]
        key_count = len(layer_info.get('keys', {}))
        log_info(
            "Layer {idx}: {name} ({count} keys configured)".format(
                idx=self.current_layer, name=get_layer_name(self.current_layer), count=key_count
            )
        )

    def _adjust_brightness(self, delta):
        """Adjust LED brightness."""
        # Clamp brightness and apply
        try:
            current = getattr(self, 'brightness', 1.0) or 1.0
            self.brightness = max(0.1, min(1.0, current + delta))
            log_info("Brightness: {:.1f}".format(self.brightness))
            self.update_layer_colors()
        except Exception as e:
            log_error(f"Failed to adjust brightness: {e}")

    def release_all_keys(self):
        """Release all currently pressed keys and turn off all LEDs."""
        try:
            # Release all currently pressed keys
            self.keyboard.release_all()
            log_info("Released all pressed keys")
            
            # Turn off all LEDs
            for key in self.keys:
                key.led_off()
            log_info("All LEDs turned off")
            
            # Clear tracking sets
            self.pressed_keys.clear()
            self.held_keys.clear()
            
        except Exception as e:
            log_error(f"Error during cleanup: {e}")

    def run(self):
        """Main run loop."""
        log_info("\n" + "="*50)
        log_info("Keybow Controller Starting")
        log_info("="*50)
        log_info(f"Current layer: {self.current_layer} ({get_layer_name(self.current_layer)})")
        if self.modifier_key_num is not None:
            log_info("Hold modifier key + layer key to switch layers")
        log_info("Press Ctrl+C to stop")
        log_info("="*50 + "\n")
        
        try:
            while True:
                self.keybow.update()
        except KeyboardInterrupt:
            log_info("Keybow Controller stopped by user")
            self.release_all_keys()  # Clean up on exit
        except Exception as e:
            log_error(f"Unexpected error: {e}")
            self.release_all_keys()  # Clean up on error
            log_info("Restarting in 3 seconds...")
            time.sleep(3)
            self.run()  # Restart

def main():
    """Main entry point with error handling."""
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            controller = KeybowController()
            controller.run()
            break  # If we get here, the program ran successfully and was stopped by user
        except Exception as e:
            retry_count += 1
            log_error(f"Fatal error starting Keybow controller: {e}")
            
            if retry_count < max_retries:
                log_info(f"Attempting recovery... (attempt {retry_count}/{max_retries})")
                time.sleep(2)
                
                # Try supervisor reload for certain errors
                if "in use" in str(e) or "unexpected keyword argument" in str(e):
                    try:
                        import supervisor
                        log_info("Reloading supervisor...")
                        supervisor.reload()
                    except:
                        log_error("Supervisor reload not available")
            else:
                log_error("Maximum retry attempts reached. Please check hardware and restart manually.")
                break

if __name__ == "__main__":
    main()
