# Media and Streaming Layer Example
# Controls for audio, video, and streaming applications
# Copy these definitions into your main config file and adapt as needed

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from constants import ActionType, Key, Color, LayerAction

# Media Layer Configuration (use layer index 1, 2, 3, etc. in your main config)
MEDIA_LAYER = {
    'name': 'Media',
    'description': 'Audio, video, and streaming controls',
    'color': Color.ORANGE,  # Media orange theme
    'keys': {
        # Media playback controls (top row)
        Key.R3C3: {  # Previous Track
            'action_type': ActionType.CONSUMER,
            'action': ConsumerControlCode.SCAN_PREVIOUS_TRACK,
            'colors': {
                'default': (255, 100, 0),      # Orange theme
                'pressed': (255, 150, 50),
                'held': (255, 200, 100)
            }
        },
        Key.R2C3: {  # Play/Pause
            'action_type': ActionType.CONSUMER,
            'action': ConsumerControlCode.PLAY_PAUSE,
            'colors': {
                'default': (255, 120, 0),
                'pressed': (255, 170, 50),
                'held': (255, 220, 100)
            }
        },
        Key.R1C3: {  # Next Track
            'action_type': ActionType.CONSUMER,
            'action': ConsumerControlCode.SCAN_NEXT_TRACK,
            'colors': {
                'default': (255, 140, 0),
                'pressed': (255, 190, 50),
                'held': (255, 240, 100)
            }
        },
        Key.R0C3: {  # Stop
            'action_type': ActionType.CONSUMER,
            'action': ConsumerControlCode.STOP,
            'colors': {
                'default': (255, 80, 0),
                'pressed': (255, 130, 50),
                'held': (255, 180, 100)
            }
        },
        
        # Volume controls (second row)
        Key.R3C2: {  # Mute
            'action_type': ActionType.CONSUMER,
            'action': ConsumerControlCode.MUTE,
            'colors': {
                'default': (200, 100, 0),
                'pressed': (255, 150, 50),
                'held': (255, 200, 100)
            }
        },
        Key.R2C2: {  # Volume Down
            'action_type': ActionType.CONSUMER,
            'action': ConsumerControlCode.VOLUME_DECREMENT,
            'colors': {
                'default': (200, 120, 0),
                'pressed': (255, 170, 50),
                'held': (255, 220, 100)
            }
        },
        Key.R1C2: {  # Volume Up
            'action_type': ActionType.CONSUMER,
            'action': ConsumerControlCode.VOLUME_INCREMENT,
            'colors': {
                'default': (200, 140, 0),
                'pressed': (255, 190, 50),
                'held': (255, 240, 100)
            }
        },
        Key.R1C3: {  # Mic Mute (Windows key + M for Windows)
            'action_type': ActionType.KEY,
            'action': [Keycode.WINDOWS, Keycode.M],
            'colors': {
                'default': (200, 80, 0),
                'pressed': (255, 130, 50),
                'held': (255, 180, 100)
            }
        },
        
        # Streaming shortcuts (third row)
        Key.R3C1: {  # OBS Scene 1
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.ONE],
            'colors': {
                'default': (150, 100, 0),
                'pressed': (200, 150, 50),
                'held': (255, 200, 100)
            }
        },
        Key.R2C1: {  # OBS Scene 2
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.TWO],
            'colors': {
                'default': (150, 120, 0),
                'pressed': (200, 170, 50),
                'held': (255, 220, 100)
            }
        },
        Key.R2C2: {  # OBS Start/Stop Recording
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.R],
            'colors': {
                'default': (150, 140, 0),
                'pressed': (200, 190, 50),
                'held': (255, 240, 100)
            }
        },
        Key.R2C3: {  # OBS Start/Stop Streaming
            'action_type': ActionType.KEY,
            'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.S],
            'colors': {
                'default': (150, 80, 0),
                'pressed': (200, 130, 50),
                'held': (255, 180, 100)
            }
        },
        
        # Layer navigation (bottom row)
        Key.R3C0: {  # Modifier key
            'action_type': ActionType.LAYER,
            'action': LayerAction.MODIFIER,
            'colors': {
                'default': (100, 50, 0),
                'pressed': (150, 100, 50),
                'held': (200, 150, 100)
            }
        },
        Key.R3C1: {  # Back to main layer (adjust target as needed)
            'action_type': ActionType.LAYER,
            'action': 0,  # Change this to your main layer index
            'colors': {
                'default': (110, 60, 0),
                'pressed': (160, 110, 50),
                'held': (210, 160, 100)
            }
        },
        Key.R3C2: {  # Discord Push-to-Talk (customize key as needed)
            'action_type': ActionType.KEY,
            'action': [Keycode.GRAVE_ACCENT],  # Backtick key - change as needed
            'colors': {
                'default': (120, 70, 0),
                'pressed': (170, 120, 50),
                'held': (220, 170, 100)
            }
        },
        Key.R3C3: {  # Screenshot
            'action_type': ActionType.KEY,
            'action': [Keycode.WINDOWS, Keycode.SHIFT, Keycode.S],
            'colors': {
                'default': (130, 80, 0),
                'pressed': (180, 130, 50),
                'held': (230, 180, 100)
            }
        }
    }
}

# Example usage in main config:
# LAYERS = {
#     0: { ... your main layer ... },
#     1: MEDIA_LAYER,  # Media and streaming layer
#     # ... other layers ...
# }
