# Text and Productivity Layer Example
# Text snippets, shortcuts, and productivity tools
# Copy these definitions into your main config file and adapt as needed

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from constants import ActionType, Key, Color, LayerAction

# Text/Productivity Layer Configuration (use layer index 1, 2, 3, etc. in your main config)
TEXT_LAYER = {
    'name': 'Text & Productivity',
    'description': 'Text snippets, shortcuts, and productivity tools',
    'color': Color.GREEN,  # Green productivity theme
    'keys': {
        # Common text snippets (top row)
        Key.R3C3: {  # Email signature
            'action_type': ActionType.STRING,
            'action': "Best regards,\nYour Name",
            'colors': {
                'default': (0, 200, 100),      # Green theme
                'pressed': (50, 255, 150),
                'held': (100, 255, 200)
            }
        },
        Key.R2C3: {  # Current date
            'action_type': ActionType.FUNCTION,
            'action': 'type_current_date',  # Custom function (would need implementation)
            'colors': {
                'default': (0, 180, 120),
                'pressed': (50, 230, 170),
                'held': (100, 255, 220)
            }
        },
        Key.R1C3: {  # Common greeting
            'action_type': ActionType.STRING,
            'action': "Hello,\n\nI hope this message finds you well.",
            'colors': {
                'default': (0, 160, 140),
                'pressed': (50, 210, 190),
                'held': (100, 255, 240)
            }
        },
        Key.R0C3: {  # Meeting template
            'action_type': ActionType.STRING,
            'action': "## Meeting Notes\n\n**Date:** \n**Attendees:** \n**Agenda:** \n\n**Action Items:** \n- ",
            'colors': {
                'default': (0, 140, 160),
                'pressed': (50, 190, 210),
                'held': (100, 240, 255)
            }
        },
        
        # Common shortcuts (second row)
        Key.R3C2: {  # Select All
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.A],
            'colors': {
                'default': (20, 200, 100),
                'pressed': (70, 255, 150),
                'held': (120, 255, 200)
            }
        },
        Key.R2C2: {  # Copy
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.C],
            'colors': {
                'default': (20, 180, 120),
                'pressed': (70, 230, 170),
                'held': (120, 255, 220)
            }
        },
        Key.R1C2: {  # Paste
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.V],
            'colors': {
                'default': (20, 160, 140),
                'pressed': (70, 210, 190),
                'held': (120, 255, 240)
            }
        },
        Key.R1C3: {  # Undo
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.Z],
            'colors': {
                'default': (20, 140, 160),
                'pressed': (70, 190, 210),
                'held': (120, 240, 255)
            }
        },
        
        # Navigation and window management (third row)
        Key.R3C1: {  # Alt+Tab (Window Switcher)
            'action_type': ActionType.KEY,
            'action': [Keycode.ALT, Keycode.TAB],
            'colors': {
                'default': (40, 200, 100),
                'pressed': (90, 255, 150),
                'held': (140, 255, 200)
            }
        },
        Key.R2C1: {  # Windows + Left (Snap Left)
            'action_type': ActionType.KEY,
            'action': [Keycode.WINDOWS, Keycode.LEFT_ARROW],
            'colors': {
                'default': (40, 180, 120),
                'pressed': (90, 230, 170),
                'held': (140, 255, 220)
            }
        },
        Key.R2C2: {  # Windows + Right (Snap Right)
            'action_type': ActionType.KEY,
            'action': [Keycode.WINDOWS, Keycode.RIGHT_ARROW],
            'colors': {
                'default': (40, 160, 140),
                'pressed': (90, 210, 190),
                'held': (140, 255, 240)
            }
        },
        Key.R2C3: {  # Windows + D (Show Desktop)
            'action_type': ActionType.KEY,
            'action': [Keycode.WINDOWS, Keycode.D],
            'colors': {
                'default': (40, 140, 160),
                'pressed': (90, 190, 210),
                'held': (140, 240, 255)
            }
        },
        
        # Layer navigation (bottom row)
        Key.R3C0: {  # Modifier key
            'action_type': ActionType.LAYER,
            'action': LayerAction.MODIFIER,
            'colors': {
                'default': (0, 100, 50),
                'pressed': (50, 150, 100),
                'held': (100, 200, 150)
            }
        },
        Key.R3C1: {  # Back to main layer (adjust target as needed)
            'action_type': ActionType.LAYER,
            'action': 0,  # Change this to your main layer index
            'colors': {
                'default': (0, 110, 60),
                'pressed': (50, 160, 110),
                'held': (100, 210, 160)
            }
        },
        Key.R3C2: {  # Calculator shortcut
            'action_type': ActionType.KEY,
            'action': [Keycode.WINDOWS, Keycode.R],  # Opens Run dialog
            'colors': {
                'default': (0, 120, 70),
                'pressed': (50, 170, 120),
                'held': (100, 220, 170)
            }
        },
        Key.R3C3: {  # Task Manager
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE],
            'colors': {
                'default': (0, 130, 80),
                'pressed': (50, 180, 130),
                'held': (100, 230, 180)
            }
        }
    }
}

# Example usage in main config:
# LAYERS = {
#     0: { ... your main layer ... },
#     1: TEXT_LAYER,  # Text and productivity layer
#     # ... other layers ...
# }
