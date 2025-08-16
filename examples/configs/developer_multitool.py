# Developer Multi-Tool Configuration
# Layer 0: Code shortcuts, Layer 1: Debug tools, Layer 2: Terminal commands, Layer 3: Documentation

from adafruit_hid.keycode import Keycode
from constants import ActionType, Key, Color, LayerAction, get_layer_name, get_config_info

# Layer definitions
LAYERS = {
    0: {  # Code shortcuts layer
        'name': 'Code Editor',
        'description': 'Common IDE and editor shortcuts',
        'color': Color.BLUE,
        'keys': {
            # Top row: File operations
            Key.R3C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.N],  # New file
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.O],  # Open file
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.S],  # Save
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R0C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.S],  # Save All
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            # Second row: Code navigation
            Key.R3C2: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.G],  # Go to line
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.F],  # Find in files
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
            Key.R1C2: {
                'action_type': ActionType.KEY,
                'action': [Keycode.F12],  # Go to definition
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.SHIFT, Keycode.F12],  # Find references
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            # Third row: Code editing
            Key.R3C1: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.FORWARD_SLASH],  # Comment toggle
                'colors': {'default': Color.ORANGE, 'pressed': Color.WHITE}
            },
            Key.R2C1: {
                'action_type': ActionType.KEY,
                'action': [Keycode.ALT, Keycode.SHIFT, Keycode.F],  # Format document
                'colors': {'default': Color.ORANGE, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.LAYER,
                'action': 1,  # Switch to Debug layer
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.LAYER,
                'action': 2,  # Switch to Terminal layer
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            # Bottom row: Modifier and utilities
            Key.R3C0: {
                'action_type': ActionType.LAYER,
                'action': LayerAction.MODIFIER,
                'colors': {'default': Color.WHITE, 'pressed': Color.BLUE}
            },
            Key.R3C1: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.P],  # Command palette
                'colors': {'default': Color.CYAN, 'pressed': Color.WHITE}
            },
            Key.R3C2: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.GRAVE_ACCENT],  # Toggle terminal
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R3C3: {
                'action_type': ActionType.LAYER,
                'action': 3,  # Switch to Documentation layer
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
        }
    },
    1: {  # Debug tools layer
        'name': 'Debug Tools',
        'description': 'Debugging and testing shortcuts',
        'color': Color.RED,
        'keys': {
            # Top row: Breakpoint controls
            Key.R3C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.F9,  # Toggle breakpoint
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.F9],  # Remove all breakpoints
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.KEY,
                'action': Keycode.F5,  # Start debugging
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R0C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.SHIFT, Keycode.F5],  # Stop debugging
                'colors': {'default': Color.ORANGE, 'pressed': Color.WHITE}
            },
            # Second row: Step controls
            Key.R3C2: {
                'action_type': ActionType.KEY,
                'action': Keycode.F10,  # Step over
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.KEY,
                'action': Keycode.F11,  # Step into
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R1C2: {
                'action_type': ActionType.KEY,
                'action': [Keycode.SHIFT, Keycode.F11],  # Step out
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.F5],  # Continue
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            # Third row: Testing and build
            Key.R3C1: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.T],  # Run tests
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            Key.R2C1: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.B],  # Build
                'colors': {'default': Color.ORANGE, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.LAYER,
                'action': 0,  # Back to Code layer
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.LAYER,
                'action': 2,  # Switch to Terminal layer
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            # Bottom row: Modifier and utilities
            Key.R3C0: {
                'action_type': ActionType.LAYER,
                'action': LayerAction.MODIFIER,
                'colors': {'default': Color.WHITE, 'pressed': Color.RED}
            },
            Key.R3C1: {
                'action_type': ActionType.KEY,
                'action': [Keycode.ALT, Keycode.F4],  # Close application
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R3C2: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.R],  # Run without debugging
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R3C3: {
                'action_type': ActionType.LAYER,
                'action': 3,  # Switch to Documentation layer
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
        }
    },
    2: {  # Terminal commands layer
        'name': 'Terminal',
        'description': 'Common terminal and Git commands',
        'color': Color.GREEN,
        'keys': {
            # Top row: Git commands
            Key.R3C3: {
                'action_type': ActionType.STRING,
                'action': "git status",
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.STRING,
                'action': "git add .",
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.STRING,
                'action': "git commit -m \"\"",
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R0C3: {
                'action_type': ActionType.STRING,
                'action': "git push",
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            # Second row: Directory navigation
            Key.R3C2: {
                'action_type': ActionType.STRING,
                'action': "ls -la",
                'colors': {'default': Color.CYAN, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.STRING,
                'action': "cd ..",
                'colors': {'default': Color.CYAN, 'pressed': Color.WHITE}
            },
            Key.R1C2: {
                'action_type': ActionType.STRING,
                'action': "pwd",
                'colors': {'default': Color.CYAN, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.STRING,
                'action': "clear",
                'colors': {'default': Color.WHITE, 'pressed': Color.GREEN}
            },
            # Third row: Package management and build
            Key.R3C1: {
                'action_type': ActionType.STRING,
                'action': "npm install",
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
            Key.R2C1: {
                'action_type': ActionType.STRING,
                'action': "npm run dev",
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.LAYER,
                'action': 0,  # Back to Code layer
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.LAYER,
                'action': 1,  # Switch to Debug layer
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            # Bottom row: Modifier and utilities
            Key.R3C0: {
                'action_type': ActionType.LAYER,
                'action': LayerAction.MODIFIER,
                'colors': {'default': Color.WHITE, 'pressed': Color.GREEN}
            },
            Key.R3C1: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.C],  # Cancel command
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R3C2: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.L],  # Clear terminal
                'colors': {'default': Color.WHITE, 'pressed': Color.GREEN}
            },
            Key.R3C3: {
                'action_type': ActionType.LAYER,
                'action': 3,  # Switch to Documentation layer
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
        }
    },
    3: {  # Documentation layer
        'name': 'Documentation',
        'description': 'Quick access to docs and references',
        'color': Color.YELLOW,
        'keys': {
            # Top row: Documentation sites
            Key.R3C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.ALT, Keycode.F1],  # MDN (set up browser bookmark)
                'colors': {'default': Color.YELLOW, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.ALT, Keycode.F2],  # Stack Overflow
                'colors': {'default': Color.ORANGE, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.ALT, Keycode.F3],  # GitHub
                'colors': {'default': Color.WHITE, 'pressed': Color.YELLOW}
            },
            Key.R0C3: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.ALT, Keycode.F4],  # Documentation portal
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            # Second row: Code snippets and templates
            Key.R3C2: {
                'action_type': ActionType.STRING,
                'action': "console.log();",
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.STRING,
                'action': "unassigned",
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R1C2: {
                'action_type': ActionType.STRING,
                'action': "unassigned",
                'colors': {'default': Color.ORANGE, 'pressed': Color.WHITE}
            },
            Key.R1C3: {
                'action_type': ActionType.STRING,
                'action': "function() {}",
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            # Third row: Common development queries
            Key.R3C1: {
                'action_type': ActionType.STRING,
                'action': "how to ",
                'colors': {'default': Color.CYAN, 'pressed': Color.WHITE}
            },
            Key.R2C1: {
                'action_type': ActionType.STRING,
                'action': "error: ",
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
            },
            Key.R2C2: {
                'action_type': ActionType.LAYER,
                'action': 0,  # Back to Code layer
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R2C3: {
                'action_type': ActionType.LAYER,
                'action': 2,  # Switch to Terminal layer
                'colors': {'default': Color.GREEN, 'pressed': Color.WHITE}
            },
            # Bottom row: Modifier and utilities
            Key.R3C0: {
                'action_type': ActionType.LAYER,
                'action': LayerAction.MODIFIER,
                'colors': {'default': Color.WHITE, 'pressed': Color.YELLOW}
            },
            Key.R3C1: {
                'action_type': ActionType.KEY,
                'action': [Keycode.CONTROL, Keycode.SHIFT, Keycode.I],  # Developer tools
                'colors': {'default': Color.PURPLE, 'pressed': Color.WHITE}
            },
            Key.R3C2: {
                'action_type': ActionType.KEY,
                'action': Keycode.F1,  # Help
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R3C3: {
                'action_type': ActionType.LAYER,
                'action': 1,  # Switch to Debug layer
                'colors': {'default': Color.RED, 'pressed': Color.WHITE}
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
    'config_name': 'Developer Multi-Tool',
    'config_description': 'Complete development environment with code, debug, terminal, and docs',
    'config_version': '1.0.0',
    'default_layer': 0,  # Start with code editor
    'modifier_key': Key.R3C0,  # Bottom-left key
    'brightness': 0.8,
    'led_sleep_enabled': True,
    'led_sleep_time': 300,  # 5 minutes for coding sessions
}
