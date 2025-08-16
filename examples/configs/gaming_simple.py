# Gaming Keys - Simple and Clean
# Layout: [ESC][TAB][Q  ][1 ]   [W ][A ][S ][D ]   [SPC][ALT][C][SFT]   [F1][F2][F3][F4]

from adafruit_hid.keycode import Keycode
from constants import Color, Key, create_simple_keymap, get_layer_name, get_config_info

# Gaming keymap: Key.RxCx -> keycode
keys = {
    Key.R0C0: Keycode.ESCAPE, Key.R0C1: Keycode.TAB, Key.R0C2: Keycode.Q, Key.R0C3: Keycode.ONE,
    Key.R1C0: Keycode.W, Key.R1C1: Keycode.A, Key.R1C2: Keycode.S, Key.R1C3: Keycode.D,
    Key.R2C0: Keycode.SPACE, Key.R2C1: Keycode.ALT, Key.R2C2: Keycode.C, Key.R2C3: Keycode.SHIFT,
    Key.R3C0: Keycode.F1, Key.R3C1: Keycode.F2, Key.R3C2: Keycode.F3, Key.R3C3: Keycode.F4
}

# Gaming colors: WASD=green, space/shift=blue, functions=red, others=white  
wasd_keys = [Key.R1C0, Key.R1C1, Key.R1C2, Key.R1C3]
action_keys = [Key.R2C0, Key.R2C3]  # Space, Shift
function_keys = [Key.R3C0, Key.R3C1, Key.R3C2, Key.R3C3]
other_keys = [Key.R0C0, Key.R2C1, Key.R0C1, Key.R2C2, Key.R0C2, Key.R0C3]
colors = {}
# WASD (green)
for k in wasd_keys:
    colors[k] = Color.GREEN
# Space, Shift (blue)
for k in action_keys:
    colors[k] = Color.BLUE
# Function keys (red)
for k in function_keys:
    colors[k] = Color.RED
# Others (white)
for k in other_keys:
    colors[k] = Color.WHITE

# Generate full configuration
LAYERS, COLORS, CONFIG = create_simple_keymap(keys, colors, "Gaming Keys")
