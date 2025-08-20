


from adafruit_hid.keycode import Keycode
from constants import Color, Key, create_simple_keymap

# Layer 0 - Main (blue)
main_keys = {
    Key.R0C0: Keycode.A,
    Key.R0C1: Keycode.B,
    Key.R0C2: Keycode.C,
    Key.R0C3: Keycode.D,
}
main_colors = {k: Color.BLUE for k in main_keys}
LAYERS0, COLORS0, CONFIG0 = create_simple_keymap(main_keys, main_colors, "Main")

# Layer 1 - Media (green)
media_keys = {
    Key.R0C0: Keycode.F13,
    Key.R0C1: Keycode.F14,
    Key.R0C2: Keycode.F15,
    Key.R0C3: Keycode.F16,
}
media_colors = {k: Color.GREEN for k in media_keys}
LAYERS1, COLORS1, CONFIG1 = create_simple_keymap(media_keys, media_colors, "Media")

# Layer 2 - System (red)
system_keys = {
    Key.R0C0: [Keycode.CONTROL, Keycode.ALT, Keycode.DELETE],
    Key.R0C1: Keycode.ESCAPE,
    Key.R0C2: Keycode.F1,
    Key.R0C3: Keycode.F2,
}
system_colors = {k: Color.RED for k in system_keys}
LAYERS2, COLORS2, CONFIG2 = create_simple_keymap(system_keys, system_colors, "System")

# Merge layers
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
