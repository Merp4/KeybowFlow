# Developer Multi-Tool (v2)
# 3-layer configuration: Code, Debug, Terminal

from adafruit_hid.keycode import Keycode
from constants import ActionType, Key, Color, LayerAction

# Layer 0 - Code editor shortcuts (blue)
L0 = {
    'name': 'Code',
    'color': Color.BLUE,
    'keys': {
        Key.R0C0: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.N], 'colors': {'default': Color.BLUE}},
        Key.R0C1: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.O], 'colors': {'default': Color.BLUE}},
        Key.R0C2: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.S], 'colors': {'default': Color.GREEN}},
        Key.R0C3: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.S], 'colors': {'default': Color.GREEN}},

        Key.R1C0: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.G], 'colors': {'default': Color.YELLOW}},
        Key.R1C1: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.F], 'colors': {'default': Color.YELLOW}},
        Key.R1C2: {'action_type': ActionType.KEY, 'action': Keycode.F12, 'colors': {'default': Color.PURPLE}},
        Key.R1C3: {'action_type': ActionType.KEY, 'action': [Keycode.ALT, Keycode.F12], 'colors': {'default': Color.PURPLE}},

        Key.R2C0: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.Z], 'colors': {'default': Color.ORANGE}},
        Key.R2C1: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.Y], 'colors': {'default': Color.ORANGE}},
        Key.R2C2: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.D], 'colors': {'default': Color.CYAN}},
        Key.R2C3: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.K], 'colors': {'default': Color.RED}},

        # Bottom row: R3C0 is modifier for layer switch
        Key.R3C0: {'action_type': ActionType.LAYER, 'action': LayerAction.MODIFIER, 'colors': {'default': Color.WHITE}},
    Key.R3C1: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.FORWARD_SLASH], 'colors': {'default': Color.PINK}},
        Key.R3C2: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.P], 'colors': {'default': Color.WHITE}},
        Key.R3C3: {'action_type': ActionType.KEY, 'action': Keycode.ENTER, 'colors': {'default': Color.GREEN}},
    }
}

# Layer 1 - Debug tools (red)
L1 = {
    'name': 'Debug',
    'color': Color.RED,
    'keys': {
        Key.R0C0: {'action_type': ActionType.KEY, 'action': Keycode.F9, 'colors': {'default': Color.RED}},
        Key.R0C1: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.F9], 'colors': {'default': Color.RED}},
        Key.R0C2: {'action_type': ActionType.KEY, 'action': Keycode.F5, 'colors': {'default': Color.GREEN}},
        Key.R0C3: {'action_type': ActionType.KEY, 'action': [Keycode.SHIFT, Keycode.F5], 'colors': {'default': Color.ORANGE}},

        Key.R1C0: {'action_type': ActionType.KEY, 'action': Keycode.F10, 'colors': {'default': Color.BLUE}},
        Key.R1C1: {'action_type': ActionType.KEY, 'action': Keycode.F11, 'colors': {'default': Color.BLUE}},
        Key.R1C2: {'action_type': ActionType.KEY, 'action': [Keycode.SHIFT, Keycode.F11], 'colors': {'default': Color.BLUE}},
        Key.R1C3: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.F5], 'colors': {'default': Color.GREEN}},

        Key.R2C0: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.T], 'colors': {'default': Color.YELLOW}},
        Key.R2C1: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.B], 'colors': {'default': Color.CYAN}},
        Key.R2C2: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.D], 'colors': {'default': Color.PURPLE}},
        Key.R2C3: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.R], 'colors': {'default': Color.RED}},

        Key.R3C0: {'action_type': ActionType.LAYER, 'action': LayerAction.MODIFIER, 'colors': {'default': Color.WHITE}},
        Key.R3C1: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.I], 'colors': {'default': Color.WHITE}},
        Key.R3C2: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.C], 'colors': {'default': Color.WHITE}},
        Key.R3C3: {'action_type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.P], 'colors': {'default': Color.WHITE}},
    }
}

# Layer 2 - Terminal macros (cyan)
L2 = {
    'name': 'Terminal',
    'color': Color.CYAN,
    'keys': {
        Key.R0C0: {'action_type': ActionType.STRING, 'action': 'git status\n', 'colors': {'default': Color.CYAN}},
        Key.R0C1: {'action_type': ActionType.STRING, 'action': 'git add .\n', 'colors': {'default': Color.CYAN}},
        Key.R0C2: {'action_type': ActionType.STRING, 'action': 'git commit -m ""\n', 'colors': {'default': Color.CYAN}},
        Key.R0C3: {'action_type': ActionType.STRING, 'action': 'git push\n', 'colors': {'default': Color.CYAN}},

        Key.R1C0: {'action_type': ActionType.STRING, 'action': 'clear\n', 'colors': {'default': Color.WHITE}},
        Key.R1C1: {'action_type': ActionType.STRING, 'action': 'ls -la\n', 'colors': {'default': Color.WHITE}},
        Key.R1C2: {'action_type': ActionType.STRING, 'action': 'pwd\n', 'colors': {'default': Color.WHITE}},
        Key.R1C3: {'action_type': ActionType.STRING, 'action': 'htop\n', 'colors': {'default': Color.WHITE}},

        Key.R2C0: {'action_type': ActionType.STRING, 'action': 'pip install -r requirements.txt\n', 'colors': {'default': Color.YELLOW}},
        Key.R2C1: {'action_type': ActionType.STRING, 'action': 'npm run build\n', 'colors': {'default': Color.YELLOW}},
        Key.R2C2: {'action_type': ActionType.STRING, 'action': 'docker-compose up -d\n', 'colors': {'default': Color.YELLOW}},
        Key.R2C3: {'action_type': ActionType.STRING, 'action': 'git pull\n', 'colors': {'default': Color.YELLOW}},

        Key.R3C0: {'action_type': ActionType.LAYER, 'action': LayerAction.MODIFIER, 'colors': {'default': Color.WHITE}},
        Key.R3C1: {'action_type': ActionType.STRING, 'action': 'echo "Hello"\n', 'colors': {'default': Color.PINK}},
        Key.R3C2: {'action_type': ActionType.STRING, 'action': 'date\n', 'colors': {'default': Color.PINK}},
        Key.R3C3: {'action_type': ActionType.KEY, 'action': Keycode.ENTER, 'colors': {'default': Color.GREEN}},
    }
}

LAYERS = {0: L0, 1: L1, 2: L2}
CONFIG = {'default_layer': 0, 'modifier_key': Key.R3C0, 'led_brightness': 0.6}

COLORS = {0: Color.BLUE, 1: Color.RED, 2: Color.CYAN}

# Required stubs for code.py compatibility
