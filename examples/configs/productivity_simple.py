# Productivity Shortcuts - Simple and Clean  
# Layout: [^C][^V][^Z ][^Y ]   [^X][^A][^S][^F ]   [^B][^I][^U][DEL]   [HOME][END][PGUP][PGDN]

from adafruit_hid.keycode import Keycode
from constants import Color, Key, create_simple_keymap, get_layer_name, get_config_info

# Productivity keymap: Key.RxCx -> keycode (shortcuts as key combinations)
keys = {
    Key.R0C0: [Keycode.CONTROL, Keycode.C], Key.R0C1: [Keycode.CONTROL, Keycode.V], Key.R0C2: [Keycode.CONTROL, Keycode.Z], Key.R0C3: [Keycode.CONTROL, Keycode.Y],
    Key.R1C0: [Keycode.CONTROL, Keycode.X], Key.R1C1: [Keycode.CONTROL, Keycode.A], Key.R1C2: [Keycode.CONTROL, Keycode.S], Key.R1C3: [Keycode.CONTROL, Keycode.F],
    Key.R2C0: [Keycode.CONTROL, Keycode.B], Key.R2C1: [Keycode.CONTROL, Keycode.I], Key.R2C2: [Keycode.CONTROL, Keycode.U], Key.R2C3: Keycode.DELETE,
    Key.R3C0: Keycode.HOME, Key.R3C1: Keycode.END, Key.R3C2: Keycode.PAGE_UP, Key.R3C3: Keycode.PAGE_DOWN
}

# Productivity colors: edit=blue, format=green, nav=yellow, delete=red
edit_keys = [Key.R0C0, Key.R0C1, Key.R0C2, Key.R0C3, Key.R1C0, Key.R1C1, Key.R1C2, Key.R1C3]
format_keys = [Key.R2C0, Key.R2C1, Key.R2C2]
nav_keys = [Key.R3C0, Key.R3C1, Key.R3C2, Key.R3C3]
colors = {}
# Edit shortcuts (blue)
for k in edit_keys:
    colors[k] = Color.BLUE
# Format shortcuts (green)
for k in format_keys:
    colors[k] = Color.GREEN
# Navigation (yellow)
for k in nav_keys:
    colors[k] = Color.YELLOW
# Delete (red)
colors[Key.R2C3] = Color.RED

# Generate full configuration
LAYERS, COLORS, CONFIG = create_simple_keymap(keys, colors, "Productivity")
