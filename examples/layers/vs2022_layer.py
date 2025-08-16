# Visual Studio 2022 Layer Example
# Purple-themed layer for Visual Studio 2022 shortcuts and actions
# Copy these definitions into your main config file and adapt as needed

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from constants import ActionType, Key, Color, LayerAction

# Visual Studio 2022 Layer Configuration (use layer index 1, 2, 3, etc. in your main config)
VS2022_LAYER = {
    'name': 'Visual Studio',
    'description': 'Visual Studio 2022 shortcuts and commands',
    'color': Color.PURPLE,  # VS2022 purple theme
    'keys': {
        # Solution and project operations (top row)
        Key.R3C3: {  # Build Solution
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.B],
            'colors': {
                'default': (150, 0, 200),      # VS2022 purple
                'pressed': (200, 50, 255),
                'held': (255, 100, 255)
            }
        },
        Key.R2C3: {  # Quick Launch
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.Q],
            'colors': {
                'default': (130, 0, 180),
                'pressed': (180, 50, 230),
                'held': (230, 100, 255)
            }
        },
        Key.R1C3: {  # Go to All
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.T],
            'colors': {
                'default': (170, 0, 160),
                'pressed': (220, 50, 210),
                'held': (255, 100, 255)
            }
        },
        Key.R0C3: {  # Solution Explorer
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.ALT, Keycode.L],
            'colors': {
                'default': (140, 0, 140),
                'pressed': (190, 50, 190),
                'held': (240, 100, 240)
            }
        },
        
        # Code navigation and IntelliSense (second row)
        Key.R3C2: {  # Go to Definition
            'action_type': ActionType.KEY,
            'action': [Keycode.F12],
            'colors': {
                'default': (150, 20, 200),
                'pressed': (200, 70, 255),
                'held': (255, 120, 255)
            }
        },
        Key.R2C2: {  # Find All References
            'action_type': ActionType.KEY,
            'action': [Keycode.SHIFT, Keycode.F12],
            'colors': {
                'default': (130, 20, 180),
                'pressed': (180, 70, 230),
                'held': (230, 120, 255)
            }
        },
        Key.R1C2: {  # Quick Info
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.K, Keycode.I],
            'colors': {
                'default': (170, 20, 160),
                'pressed': (220, 70, 210),
                'held': (255, 120, 255)
            }
        },
        Key.R1C3: {  # Peek Definition
            'action_type': ActionType.KEY,
            'action': [Keycode.ALT, Keycode.F12],
            'colors': {
                'default': (140, 20, 140),
                'pressed': (190, 70, 190),
                'held': (240, 120, 240)
            }
        },
        
        # Debugging and testing (third row)
        Key.R3C1: {  # Start Debugging
            'action_type': ActionType.KEY,
            'action': [Keycode.F5],
            'colors': {
                'default': (150, 40, 200),
                'pressed': (200, 90, 255),
                'held': (255, 140, 255)
            }
        },
        Key.R2C1: {  # Start Without Debugging
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.F5],
            'colors': {
                'default': (130, 40, 180),
                'pressed': (180, 90, 230),
                'held': (230, 140, 255)
            }
        },
        Key.R2C2: {  # Toggle Breakpoint
            'action_type': ActionType.KEY,
            'action': [Keycode.F9],
            'colors': {
                'default': (170, 40, 160),
                'pressed': (220, 90, 210),
                'held': (255, 140, 255)
            }
        },
        Key.R2C3: {  # Run All Tests
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.R, Keycode.A],
            'colors': {
                'default': (140, 40, 140),
                'pressed': (190, 90, 190),
                'held': (240, 140, 240)
            }
        },
        
        # Layer navigation and tools (bottom row)
        Key.R3C0: {  # Modifier key
            'action_type': ActionType.LAYER,
            'action': LayerAction.MODIFIER,
            'colors': {
                'default': (100, 0, 150),
                'pressed': (150, 50, 200),
                'held': (200, 100, 255)
            }
        },
        Key.R3C1: {  # Back to main layer (adjust target as needed)
            'action_type': ActionType.LAYER,
            'action': 0,  # Change this to your main layer index
            'colors': {
                'default': (110, 0, 160),
                'pressed': (160, 50, 210),
                'held': (210, 100, 255)
            }
        },
        Key.R3C2: {  # Code Cleanup
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.K, Keycode.CONTROL, Keycode.D],
            'colors': {
                'default': (120, 0, 170),
                'pressed': (170, 50, 220),
                'held': (220, 100, 255)
            }
        },
        Key.R3C3: {  # Error List
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.BACKSLASH, Keycode.E],
            'colors': {
                'default': (130, 0, 180),
                'pressed': (180, 50, 230),
                'held': (230, 100, 255)
            }
        }
    }
}

# Example usage in main config:
# LAYERS = {
#     0: { ... your main layer ... },
#     1: VS2022_LAYER,  # Visual Studio 2022 layer
#     # ... other layers ...
# }
