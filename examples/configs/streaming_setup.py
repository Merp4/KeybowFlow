# Streaming Multi-Layer Configuration
# Perfect for streamers/content creators
# Layer 0: Stream controls, Layer 1: Media controls, Layer 2: Chat/Social

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from constants import ActionType, Key, Color, LayerAction, get_layer_name, get_config_info

# Layer definitions
LAYERS = {
    0: {  # Stream Control layer
        'name': 'Stream Control',
        'description': 'OBS and streaming controls',
        'color': Color.PURPLE,
        'keys': {
            # Top row: Scene switches (F13-F16 commonly used for OBS hotkeys)
            Key.R3C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.F13,  # Scene 1
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.F14,  # Scene 2
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.F15,  # Scene 3
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            Key.R0C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.F16,  # Scene 4
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            # Second row: Source toggles
            Key.R3C2: {
                'action_type': ActionType.KEY,
                'action': Keycode.F17,  # Toggle Camera
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.KEY,
                'action': Keycode.F18,  # Toggle Mic
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R1C2: {
                'action_type': ActionType.KEY,
                'action': Keycode.F19,  # Toggle Desktop Audio
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.F20,  # Toggle Recording
                'colors': {'default': Color.ORANGE, 'pressed': Color.WHITE}
            },
            # Third row: Stream actions
            Key.R3C1: {
                'action_type': ActionType.KEY,
                'action': Keycode.F21,  # Start/Stop Stream
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R2C1: {
                'action_type': ActionType.KEY,
                'action': Keycode.F22,  # Start/Stop Recording
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.LAYER,
                'action': 1,  # Switch to Media layer
                'colors': {'default': Color.CYAN, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.LAYER,
                'action': 2,  # Switch to Chat layer
                'colors': {'default': Color.PINK, 'pressed': Color.WHITE}
            },
            # Bottom row: Modifier and utility
            Key.R3C0: {
                'action_type': ActionType.LAYER,
                'action': LayerAction.MODIFIER,
                'colors': {'default': Color.WHITE, 'pressed': Color.PURPLE}
            },
            Key.R3C1: {
                'action_type': ActionType.STRING,
                'action': "Thanks for following!",
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R3C2: {
                'action_type': ActionType.STRING,
                'action': "!discord",
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R3C3: {
                'action_type': ActionType.STRING,
                'action': "!socials",
                'colors': {'default': Color.ORANGE, 'pressed': Color.WHITE}
            },
        }
    },
    1: {  # Media Control layer
        'name': 'Media Control',
        'description': 'Audio and video playback controls',
        'color': Color.ORANGE,
        'keys': {
            # Top row: Volume and playback
            Key.R3C3: {
                'action_type': ActionType.CONSUMER,
                'action': ConsumerControlCode.VOLUME_DECREMENT,
                'colors': {'default': Color.ORANGE, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.CONSUMER,
                'action': ConsumerControlCode.VOLUME_INCREMENT,
                'colors': {'default': Color.ORANGE, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.CONSUMER,
                'action': ConsumerControlCode.MUTE,
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R0C3: {
                'action_type': ActionType.CONSUMER,
                'action': ConsumerControlCode.PLAY_PAUSE,
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            # Second row: Track controls
            Key.R3C2: {
                'action_type': ActionType.CONSUMER,
                'action': ConsumerControlCode.SCAN_PREVIOUS_TRACK,
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.CONSUMER,
                'action': ConsumerControlCode.SCAN_NEXT_TRACK,
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R1C2: {
                'action_type': ActionType.CONSUMER,
                'action': ConsumerControlCode.STOP,
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.ALT, Keycode.TAB],  # App switcher
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
            # Third row: Spotify/Media app shortcuts
            Key.R3C1: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.ALT, Keycode.F1],  # Spotify
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R2C1: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.ALT, Keycode.F2],  # YouTube Music
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.LAYER,
                'action': 0,  # Back to Stream layer
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.LAYER,
                'action': 2,  # Switch to Chat layer
                'colors': {'default': Color.PINK, 'pressed': Color.WHITE}
            },
            # Bottom row: Modifier and utility
            Key.R3C0: {
                'action_type': ActionType.LAYER,
                'action': LayerAction.MODIFIER,
                'colors': {'default': Color.WHITE, 'pressed': Color.ORANGE}
            },
            Key.R3C1: {
                'action_type': ActionType.KEY,
                'action': [Keycode.GUI, Keycode.L],  # Lock screen
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R3C2: {
                'action_type': ActionType.KEY,
                'action': [Keycode.GUI, Keycode.D],  # Show desktop
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R3C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE],  # Task Manager
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
        }
    },
    2: {  # Chat/Social layer
        'name': 'Chat & Social',
        'description': 'Chat commands and social media shortcuts',
        'color': Color.PINK,
        'keys': {
            # Top row: Common chat commands
            Key.R3C3: {
                'action_type': ActionType.STRING,
                'action': "!commands",
                'colors': {'default': Color.PINK, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.STRING,
                'action': "!lurk",
                'colors': {'default': Color.PINK, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.STRING,
                'action': "!unlurk", 
                'colors': {'default': Color.PINK, 'pressed': Color.WHITE}
            },
            Key.R0C3: {
                'action_type': ActionType.STRING,
                'action': "!schedule",
                'colors': {'default': Color.PINK, 'pressed': Color.WHITE}
            },
            # Second row: Social links
            Key.R3C2: {
                'action_type': ActionType.STRING,
                'action': "!twitter",
                'colors': {'default': Color.CYAN, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.STRING,
                'action': "!youtube",
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R1C2: {
                'action_type': ActionType.STRING,
                'action': "!discord",
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.STRING,
                'action': "!github",
                'colors': {'default': Color.WHITE, 'pressed': Color.PINK}
            },
            # Third row: Reactions and moderator tools
            Key.R3C1: {
                'action_type': ActionType.STRING,
                'action': "Thanks for the follow! ❤️",
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R2C1: {
                'action_type': ActionType.STRING,
                'action': "Thanks for the sub!",
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.LAYER,
                'action': 0,  # Back to Stream layer
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.LAYER,
                'action': 1,  # Switch to Media layer
                'colors': {'default': Color.ORANGE, 'pressed': Color.WHITE}
            },
            # Bottom row: Modifier and utility
            Key.R3C0: {
                'action_type': ActionType.LAYER,
                'action': LayerAction.MODIFIER,
                'colors': {'default': Color.WHITE, 'pressed': Color.PINK}
            },
            Key.R3C1: {
                'action_type': ActionType.STRING,
                'action': "/timeout @",
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
            Key.R3C2: {
                'action_type': ActionType.STRING,
                'action': "/ban @",
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R3C3: {
                'action_type': ActionType.STRING,
                'action': "/clear",
                'colors': {'default': Color.ORANGE, 'pressed': Color.WHITE}
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
    Color.PINK: (255, 0, 128),
}

# Configuration
CONFIG = {
    'config_name': 'Streaming Multi-Tool',
    'config_description': 'Complete streaming setup with OBS, media, and chat controls',
    'config_version': '1.0.0',
    'default_layer': 0,  # Start with stream controls
    'modifier_key': Key.R3C0,  # Bottom-left key
    'brightness': 0.9,
    'led_sleep_enabled': True,
    'led_sleep_time': 120,  # Longer for streaming sessions
}
