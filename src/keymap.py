





# KeybowFlow Multi-Layer Example
# --------------------------------
# - Modifier key (hold to enable layer switching): Key.R1C0 (bottom left)
# - Layer select keys: Key.R0C1 (top, second from left), Key.R0C2 (top, third from left)
# - Dual-action keys: normal action, or layer switch when modifier is held

from adafruit_hid.keycode import Keycode
from constants import Color, Key, LayerAction, create_simple_keymap

# Layer 0: Main (blue)
main_keys = {
    Key.R0C0: Keycode.A,
    Key.R0C1: {"default": Keycode.B, "modifier": {"action_type": "layer", "action": 1}},
    Key.R0C2: {"default": Keycode.C, "modifier": {"action_type": "layer", "action": 2}},
    Key.R0C3: Keycode.D,
        Key.R1C0: {"action_type": "modifier", "colors": {"default": Color.PURPLE}},  # Modifier key
    Key.R1C1: Keycode.E,
    Key.R1C2: Keycode.F,
    Key.R1C3: Keycode.G,
}
main_colors = {
    Key.R0C0: Color.BLUE,
    Key.R0C1: Color.YELLOW,  # Layer select key
    Key.R0C2: Color.YELLOW,  # Layer select key
    Key.R0C3: Color.BLUE,
    Key.R1C0: Color.PURPLE,  # Modifier key
    Key.R1C1: Color.BLUE,
    Key.R1C2: Color.BLUE,
    Key.R1C3: Color.BLUE,
}
LAYERS0, COLORS0, CONFIG0 = create_simple_keymap(main_keys, main_colors, "Main")

# Layer 1: Media (green)
media_keys = {
    Key.R0C0: Keycode.F13,
    Key.R0C1: {"default": Keycode.F14, "modifier": {"action_type": "layer", "action": 0}},
    Key.R0C2: Keycode.F15,
    Key.R0C3: Keycode.F16,
    Key.R1C0: {"action_type": "modifier"},
    Key.R1C1: Keycode.F17,
    Key.R1C2: Keycode.F18,
    Key.R1C3: Keycode.F19,
}
media_colors = {
    Key.R0C0: Color.GREEN,
    Key.R0C1: Color.YELLOW,  # Layer select key
    Key.R0C2: Color.GREEN,
    Key.R0C3: Color.GREEN,
    Key.R1C0: Color.PURPLE,  # Modifier key
    Key.R1C1: Color.GREEN,
    Key.R1C2: Color.GREEN,
    Key.R1C3: Color.GREEN,
}
LAYERS1, COLORS1, CONFIG1 = create_simple_keymap(media_keys, media_colors, "Media")

# Layer 2: System (red)
system_keys = {
    Key.R0C0: [Keycode.CONTROL, Keycode.ALT, Keycode.DELETE],
    Key.R0C1: {"default": Keycode.ESCAPE, "modifier": {"action_type": "layer", "action": 0}},
    Key.R0C2: Keycode.F1,
    Key.R0C3: Keycode.F2,
    Key.R1C0: {"action_type": "modifier"},
    Key.R1C1: Keycode.F3,
    Key.R1C2: Keycode.F4,
    Key.R1C3: Keycode.F5,
}
system_colors = {
    Key.R0C0: Color.RED,
    Key.R0C1: Color.YELLOW,  # Layer select key
    Key.R0C2: Color.RED,
    Key.R0C3: Color.RED,
    Key.R1C0: Color.PURPLE,  # Modifier key
    Key.R1C1: Color.RED,
    Key.R1C2: Color.RED,
    Key.R1C3: Color.RED,
}
LAYERS2, COLORS2, CONFIG2 = create_simple_keymap(system_keys, system_colors, "System")

# Merge layers and config
LAYERS = {
    0: LAYERS0[0],
    1: LAYERS1[0],
    2: LAYERS2[0],
}
COLORS = {}
COLORS.update(COLORS0)
COLORS.update(COLORS1)
COLORS.update(COLORS2)
CONFIG = CONFIG0.copy()
CONFIG['default_layer'] = 0
CONFIG['led_brightness'] = 0.7
CONFIG['lighting_mode'] = 'static'
CONFIG['debug'] = True  # Enable debug logging
