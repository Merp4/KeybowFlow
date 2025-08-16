# Ultra-Simple Numpad - Only 15 lines total!
# Layout: [7][8][9][*]  [4][5][6][-]  [1][2][3][+]  [/][0][.][⏎]

from adafruit_hid.keycode import Keycode
from constants import Color, Key, create_simple_keymap, get_layer_name, get_config_info

# Simple keymap: Key.RxCx -> keycode
keys = {
    Key.R0C0: Keycode.SEVEN, Key.R0C1: Keycode.EIGHT, Key.R0C2: Keycode.NINE, Key.R0C3: Keycode.KEYPAD_ASTERISK,
    Key.R1C0: Keycode.FOUR, Key.R1C1: Keycode.FIVE, Key.R1C2: Keycode.SIX, Key.R1C3: Keycode.KEYPAD_MINUS,
    Key.R2C0: Keycode.ONE, Key.R2C1: Keycode.TWO, Key.R2C2: Keycode.THREE, Key.R2C3: Keycode.KEYPAD_PLUS,
    Key.R3C0: Keycode.KEYPAD_FORWARD_SLASH, Key.R3C1: Keycode.ZERO, Key.R3C2: Keycode.KEYPAD_PERIOD, Key.R3C3: Keycode.ENTER
}

# Simple colors: numbers=blue, operators=yellow, enter=green
number_keys = [Key.R2C0, Key.R2C1, Key.R2C2, Key.R3C1, Key.R1C0, Key.R1C1, Key.R1C2, Key.R0C0, Key.R0C1, Key.R0C2]
operator_keys = [Key.R3C0, Key.R3C2, Key.R2C3, Key.R1C3, Key.R0C3]
colors = {}
for k in number_keys:
    colors[k] = Color.BLUE
for k in operator_keys:
    colors[k] = Color.YELLOW
colors[Key.R3C3] = Color.GREEN

# Generate full configuration
LAYERS, COLORS, CONFIG = create_simple_keymap(keys, colors, "Simple Numpad")
