# Streaming Setup
# 3-layer config: Stream Controls, Media, Chat Macros

from adafruit_hid.keycode import Keycode
from constants import ActionType, Key, Color, LayerAction

# Layer 0: Stream controls (green)
S0 = {
    'name': 'Stream',
    'color': Color.GREEN,
    'keys': {
        Key.R0C0: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.S], 'colors': {'default': Color.GREEN}},
        Key.R0C1: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.R], 'colors': {'default': Color.GREEN}},
        Key.R0C2: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.T], 'colors': {'default': Color.GREEN}},
        Key.R0C3: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.D], 'colors': {'default': Color.GREEN}},

        Key.R1C0: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.L], 'colors': {'default': Color.CYAN}},
        Key.R1C1: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.M], 'colors': {'default': Color.CYAN}},
        Key.R1C2: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.O], 'colors': {'default': Color.CYAN}},
        Key.R1C3: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.K], 'colors': {'default': Color.CYAN}},

        Key.R2C0: {'action_type': ActionType.KEY, 'action': Keycode.F1, 'colors': {'default': Color.ORANGE}},
        Key.R2C1: {'action_type': ActionType.KEY, 'action': Keycode.F2, 'colors': {'default': Color.ORANGE}},
        Key.R2C2: {'action_type': ActionType.KEY, 'action': Keycode.F3, 'colors': {'default': Color.ORANGE}},
        Key.R2C3: {'action_type': ActionType.KEY, 'action': Keycode.F4, 'colors': {'default': Color.ORANGE}},

        Key.R3C0: {'action_type': ActionType.LAYER, 'action': LayerAction.MODIFIER, 'colors': {'default': Color.WHITE}},
        Key.R3C1: {'action_type': ActionType.STRING, 'action': '!cheer 100', 'colors': {'default': Color.PINK}},
        Key.R3C2: {'action_type': ActionType.STRING, 'action': '!lurk', 'colors': {'default': Color.PINK}},
        Key.R3C3: {'action_type': ActionType.STRING, 'action': '!host', 'colors': {'default': Color.PINK}},
    }
}

# Layer 1: Media controls (blue)
S1 = {
    'name': 'Media',
    'color': Color.BLUE,
    'keys': {
        Key.R0C0: {'action_type': ActionType.CONSUMER, 'action': 'play_pause', 'colors': {'default': Color.BLUE}},
        Key.R0C1: {'action_type': ActionType.CONSUMER, 'action': 'stop', 'colors': {'default': Color.BLUE}},
        Key.R0C2: {'action_type': ActionType.CONSUMER, 'action': 'next', 'colors': {'default': Color.BLUE}},
        Key.R0C3: {'action_type': ActionType.CONSUMER, 'action': 'previous', 'colors': {'default': Color.BLUE}},

        Key.R1C0: {'action_type': ActionType.CONSUMER, 'action': 'volume_up', 'colors': {'default': Color.YELLOW}},
        Key.R1C1: {'action_type': ActionType.CONSUMER, 'action': 'volume_down', 'colors': {'default': Color.YELLOW}},
        Key.R1C2: {'action_type': ActionType.CONSUMER, 'action': 'mute', 'colors': {'default': Color.YELLOW}},
        Key.R1C3: {'action_type': ActionType.CONSUMER, 'action': 'stop', 'colors': {'default': Color.YELLOW}},

    Key.R2C0: {'action_type': ActionType.CONSUMER, 'action': 'play_pause', 'colors': {'default': Color.ORANGE}},
    Key.R2C1: {'action_type': ActionType.CONSUMER, 'action': 'next', 'colors': {'default': Color.ORANGE}},
    Key.R2C2: {'action_type': ActionType.CONSUMER, 'action': 'previous', 'colors': {'default': Color.ORANGE}},
    Key.R2C3: {'action_type': ActionType.CONSUMER, 'action': 'stop', 'colors': {'default': Color.ORANGE}},

        Key.R3C0: {'action_type': ActionType.LAYER, 'action': LayerAction.MODIFIER, 'colors': {'default': Color.WHITE}},
        Key.R3C1: {'action_type': ActionType.KEY, 'action': Keycode.F13, 'colors': {'default': Color.PURPLE}},
        Key.R3C2: {'action_type': ActionType.KEY, 'action': Keycode.F14, 'colors': {'default': Color.PURPLE}},
        Key.R3C3: {'action_type': ActionType.KEY, 'action': Keycode.F15, 'colors': {'default': Color.PURPLE}},
    }
}

# Layer 2: Chat macros (white)
S2 = {
    'name': 'Chat',
    'color': Color.WHITE,
    'keys': {
        Key.R0C0: {'action_type': ActionType.STRING, 'action': 'BRB!', 'colors': {'default': Color.PINK}},
        Key.R0C1: {'action_type': ActionType.STRING, 'action': 'Thanks for the follow!', 'colors': {'default': Color.PINK}},
        Key.R0C2: {'action_type': ActionType.STRING, 'action': 'Check the link in chat', 'colors': {'default': Color.PINK}},
        Key.R0C3: {'action_type': ActionType.STRING, 'action': 'GG', 'colors': {'default': Color.PINK}},

        Key.R1C0: {'action_type': ActionType.STRING, 'action': '!so @user', 'colors': {'default': Color.CYAN}},
        Key.R1C1: {'action_type': ActionType.STRING, 'action': '!raid', 'colors': {'default': Color.CYAN}},
        Key.R1C2: {'action_type': ActionType.STRING, 'action': '!uptime', 'colors': {'default': Color.CYAN}},
        Key.R1C3: {'action_type': ActionType.STRING, 'action': '!commands', 'colors': {'default': Color.CYAN}},

        Key.R2C0: {'action_type': ActionType.STRING, 'action': '!discord', 'colors': {'default': Color.YELLOW}},
        Key.R2C1: {'action_type': ActionType.STRING, 'action': '!twitter', 'colors': {'default': Color.YELLOW}},
        Key.R2C2: {'action_type': ActionType.STRING, 'action': '!instagram', 'colors': {'default': Color.YELLOW}},
        Key.R2C3: {'action_type': ActionType.STRING, 'action': '!donate', 'colors': {'default': Color.YELLOW}},

        Key.R3C0: {'action_type': ActionType.LAYER, 'action': LayerAction.MODIFIER, 'colors': {'default': Color.WHITE}},
        Key.R3C1: {'action_type': ActionType.STRING, 'action': '!commands', 'colors': {'default': Color.PINK}},
        Key.R3C2: {'action_type': ActionType.STRING, 'action': '!socials', 'colors': {'default': Color.PINK}},
        Key.R3C3: {'action_type': ActionType.KEY, 'action': Keycode.ENTER, 'colors': {'default': Color.GREEN}},
    }
}

LAYERS = {0: S0, 1: S1, 2: S2}
CONFIG = {'default_layer': 0, 'modifier_key': Key.R3C0, 'led_brightness': 0.6}
