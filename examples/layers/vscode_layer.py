# VS Code Layer Example
# Blue-themed layer for Visual Studio Code shortcuts and actions
# Copy these definitions into your main config file and adapt as needed

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from constants import ActionType, Key, Color, LayerAction

# VS Code Layer Configuration (use layer index 1, 2, 3, etc. in your main config)
VSCODE_LAYER = {
    'name': 'VS Code',
    'description': 'Visual Studio Code shortcuts and commands',
    'color': Color.BLUE,  # VS Code blue theme
    'keys': {
        # Navigation and file operations (top row)
        Key.R3C3: {  # Quick Open
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.P],
            'colors': {
                'default': (0, 100, 200),      # VS Code blue
                'pressed': (50, 150, 255),
                'held': (100, 200, 255)
            }
        },
        Key.R2C3: {  # Command Palette
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.P],
            'colors': {
                'default': (0, 80, 180),
                'pressed': (50, 130, 230),
                'held': (100, 180, 255)
            }
        },
        Key.R1C3: {  # Go to Line
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.G],
            'colors': {
                'default': (0, 120, 160),
                'pressed': (50, 170, 210),
                'held': (100, 220, 255)
            }
        },
        Key.R0C3: {  # Toggle Terminal
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.GRAVE_ACCENT],
            'colors': {
                'default': (0, 140, 140),
                'pressed': (50, 190, 190),
                'held': (100, 240, 240)
            }
        },
        
        # Editing and refactoring (second row)
        Key.R3C2: {  # Format Document
            'action_type': ActionType.KEY,
            'action': [Keycode.SHIFT, Keycode.ALT, Keycode.F],
            'colors': {
                'default': (20, 100, 200),
                'pressed': (70, 150, 255),
                'held': (120, 200, 255)
            }
        },
        Key.R2C2: {  # Rename Symbol
            'action_type': ActionType.KEY,
            'action': [Keycode.F2],
            'colors': {
                'default': (20, 80, 180),
                'pressed': (70, 130, 230),
                'held': (120, 180, 255)
            }
        },
        Key.R1C2: {  # Go to Definition
            'action_type': ActionType.KEY,
            'action': [Keycode.F12],
            'colors': {
                'default': (20, 120, 160),
                'pressed': (70, 170, 210),
                'held': (120, 220, 255)
            }
        },
        Key.R1C3: {  # Find References
            'action_type': ActionType.KEY,
            'action': [Keycode.SHIFT, Keycode.F12],
            'colors': {
                'default': (20, 140, 140),
                'pressed': (70, 190, 190),
                'held': (120, 240, 240)
            }
        },
        
        # Debugging and running (third row)
        Key.R3C1: {  # Start Debugging
            'action_type': ActionType.KEY,
            'action': [Keycode.F5],
            'colors': {
                'default': (40, 100, 200),
                'pressed': (90, 150, 255),
                'held': (140, 200, 255)
            }
        },
        Key.R2C1: {  # Toggle Breakpoint
            'action_type': ActionType.KEY,
            'action': [Keycode.F9],
            'colors': {
                'default': (40, 80, 180),
                'pressed': (90, 130, 230),
                'held': (140, 180, 255)
            }
        },
        Key.R2C2: {  # Step Over
            'action_type': ActionType.KEY,
            'action': [Keycode.F10],
            'colors': {
                'default': (40, 120, 160),
                'pressed': (90, 170, 210),
                'held': (140, 220, 255)
            }
        },
        Key.R2C3: {  # Step Into
            'action_type': ActionType.KEY,
            'action': [Keycode.F11],
            'colors': {
                'default': (40, 140, 140),
                'pressed': (90, 190, 190),
                'held': (140, 240, 240)
            }
        },
        
        # Layer navigation (bottom row)
        Key.R3C0: {  # Modifier key
            'action_type': ActionType.LAYER,
            'action': LayerAction.MODIFIER,
            'colors': {
                'default': (0, 50, 100),
                'pressed': (50, 100, 200),
                'held': (100, 150, 255)
            }
        },
        Key.R3C1: {  # Back to main layer (adjust target as needed)
            'action_type': ActionType.LAYER,
            'action': 0,  # Change this to your main layer index
            'colors': {
                'default': (0, 60, 120),
                'pressed': (50, 110, 220),
                'held': (100, 160, 255)
            }
        },
        Key.R3C2: {  # Quick Save All
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.K, Keycode.S],
            'colors': {
                'default': (0, 70, 140),
                'pressed': (50, 120, 240),
                'held': (100, 170, 255)
            }
        },
        Key.R3C3: {  # Close All Editors
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.K, Keycode.W],
            'colors': {
                'default': (0, 80, 160),
                'pressed': (50, 130, 255),
                'held': (100, 180, 255)
            }
        }
    }
}

# Example usage in main config:
# LAYERS = {
#     0: { ... your main layer ... },
#     1: VSCODE_LAYER,  # VS Code layer
#     # ... other layers ...
# }
