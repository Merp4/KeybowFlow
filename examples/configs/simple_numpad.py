# Simple Numpad Layout
# Layout: [7][8][9][*]  [4][5][6][-]  [1][2][3][+]  [/][0][.][⏎]

from adafruit_hid.keycode import Keycode
from constants import Color, create_simple_keymap, get_layer_name, get_config_info

# Simple keymap: position -> keycode
keys = {
    3: Keycode.SEVEN, 7: Keycode.EIGHT, 11: Keycode.NINE, 15: Keycode.KEYPAD_ASTERISK,
    2: Keycode.FOUR, 6: Keycode.FIVE, 10: Keycode.SIX, 14: Keycode.KEYPAD_MINUS,
    1: Keycode.ONE, 5: Keycode.TWO, 9: Keycode.THREE, 13: Keycode.KEYPAD_PLUS,
    0: Keycode.KEYPAD_FORWARD_SLASH, 4: Keycode.ZERO, 8: Keycode.KEYPAD_PERIOD, 12: Keycode.ENTER
}

# Simple colors: numbers=blue, operators=yellow, enter=green
colors = {}
# Add blue for numbers
for k in [1,2,3,4,5,6,7,9,10,11]:
    colors[k] = Color.BLUE
# Add yellow for operators
for k in [0,8,13,14,15]:
    colors[k] = Color.YELLOW
# Add green for enter
colors[12] = Color.GREEN

# Generate full configuration
LAYERS, COLORS, CONFIG = create_simple_keymap(keys, colors, "Simple Numpad")
