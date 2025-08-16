# Work/Gaming Multi-Layer Configuration
# Press modifier key (bottom-left) + top-right to switch between work and gaming modes
# Layer 0: Work productivity, Layer 1: Gaming controls

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from constants import ActionType, Key, Color, LayerAction, get_layer_name, get_config_info

# Layer definitions
LAYERS = {
    0: {  # Work layer
        'name': 'Work Mode', 
        'description': 'Productivity shortcuts and office tools',
        'color': Color.BLUE,
        'keys': {
            # Top row: Copy, Paste, Undo, Redo
            Key.R3C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.C],
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.V], 
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.Z],
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R0C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.Y],
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            # Second row: Cut, Select All, Save, Find
            Key.R3C2: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.X],
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.A],
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R1C2: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.S],
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.F],
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            # Third row: Navigate (Home, End, Page Up, Page Down)
            Key.R3C1: {
                'action_type': ActionType.KEY,
                'action': Keycode.HOME,
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R2C1: {
                'action_type': ActionType.KEY,
                'action': Keycode.END,
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.KEY,
                'action': Keycode.PAGE_UP,
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.PAGE_DOWN,
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            # Bottom row: Modifier, Alt+Tab, Delete, Gaming Mode Switch
            Key.R3C0: {
                'action_type': ActionType.LAYER,
                'action': LayerAction.MODIFIER,
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            Key.R3C1: {
                'action_type': ActionType.KEY,
                'action': [Keycode.ALT, Keycode.TAB],
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
            Key.R3C2: {
                'action_type': ActionType.KEY,
                'action': Keycode.DELETE,
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R3C3: {
                'action_type': ActionType.LAYER,
                'action': 1,  # Switch to gaming layer
                'colors': {'default': Color.ORANGE, 'pressed': Color.WHITE}
            },
        }
    },
    1: {  # Gaming layer
        'name': 'Gaming Mode',
        'description': 'Gaming controls and hotkeys', 
        'color': Color.RED,
        'keys': {
            # Top row: ESC, Tab, Q, Numbers
            Key.R3C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.ESCAPE,
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.TAB,
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.Q,
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R0C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.ONE,
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            # Second row: WASD movement
            Key.R3C2: {
                'action_type': ActionType.KEY,
                'action': Keycode.W,
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.KEY,
                'action': Keycode.A,
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R1C2: {
                'action_type': ActionType.KEY,
                'action': Keycode.S,
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.D,
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            # Third row: Action keys
            Key.R3C1: {
                'action_type': ActionType.KEY,
                'action': Keycode.SPACE,
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R2C1: {
                'action_type': ActionType.KEY,
                'action': Keycode.SHIFT,
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.KEY,
                'action': Keycode.CONTROL,
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.ALT,
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            # Bottom row: Modifier, F-keys, Work Mode Switch
            Key.R3C0: {
                'action_type': ActionType.LAYER,
                'action': LayerAction.MODIFIER,
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            Key.R3C1: {
                'action_type': ActionType.KEY,
                'action': Keycode.F1,
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
            Key.R3C2: {
                'action_type': ActionType.KEY,
                'action': Keycode.F2,
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
            Key.R3C3: {
                'action_type': ActionType.LAYER,
                'action': 0,  # Switch back to work layer
                'colors': {'default': Color.CYAN, 'pressed': Color.WHITE}
            },
        }
    }
}

# Color definitions
COLORS = {
    Color.OFF: (0, 0, 0),
    Color.WHITE: (255, 255, 255),
    Color.BLUE: (0, 100, 255),
    Color.GREEN: (0, 255, 100),
    Color.RED: (255, 50, 50),
    Color.YELLOW: (255, 255, 0),
    Color.PURPLE: (128, 0, 255),
    Color.ORANGE: (255, 128, 0),
    Color.CYAN: (0, 255, 255),
}

# Configuration
CONFIG = {
    'config_name': 'Work/Gaming Switch',
    'config_description': 'Dual-mode setup for work productivity and gaming',
    'config_version': '1.0.0',
    'default_layer': 0,  # Start in work mode
    'modifier_key': Key.R3C0,  # Bottom-left key
    'brightness': 0.8,
    'led_sleep_enabled': True,
    'led_sleep_time': 60,
}
