# KeybowFlow Configuration Constants
# This file contains all the constants used across configurations
# Import this in your keymap.py or configuration files

class ActionType:
    """Constants for different action types that keys can perform."""
    KEY = 'key'                 # Single keycode or key combination
    SEQUENCE = 'sequence'       # Sequence of keys/combinations
    STRING = 'string'           # Type text strings
    CONSUMER = 'consumer'       # Media/consumer controls
    LAYER = 'layer'             # Switch to different layer
    FUNCTION = 'function'       # Custom functions
    NONE = 'none'               # No action

class Key:
    """
    Constants for key positions using row/column naming.
    
    Physical device layout (4x4 grid, positions 0-15):
    [ 3] [ 7] [11] [15]  ← R0 (top row)
    [ 2] [ 6] [10] [14]  ← R1 
    [ 1] [ 5] [ 9] [13]  ← R2
    [ 0] [ 4] [ 8] [12]  ← R3 (bottom row)
     ↑    ↑    ↑    ↑
    C0   C1   C2   C3
    
    Matrix layout (Row/Column):
    R0: top row    - positions 3, 7, 11, 15
    R1: second row - positions 2, 6, 10, 14  
    R2: third row  - positions 1, 5, 9, 13
    R3: bottom row - positions 0, 4, 8, 12
    """
    
    # Row 0 (Top row, positions 3, 7, 11, 15)
    R0C0 = 3     # Top-left
    R0C1 = 7     # Top, second from left
    R0C2 = 11    # Top, third from left  
    R0C3 = 15    # Top-right
    
    # Row 1 (Second row, positions 2, 6, 10, 14)
    R1C0 = 2     # Second row, leftmost
    R1C1 = 6     # Second row, second from left
    R1C2 = 10    # Second row, third from left
    R1C3 = 14    # Second row, rightmost
    
    # Row 2 (Third row, positions 1, 5, 9, 13)
    R2C0 = 1     # Third row, leftmost
    R2C1 = 5     # Third row, second from left
    R2C2 = 9     # Third row, third from left
    R2C3 = 13    # Third row, rightmost
    
    # Row 3 (Bottom row, positions 0, 4, 8, 12)
    R3C0 = 0     # Bottom-left (typically modifier)
    R3C1 = 4     # Bottom, second from left
    R3C2 = 8     # Bottom, third from left
    R3C3 = 12    # Bottom-right

class Color:
    """Constants for predefined LED colors."""
    # Basic colors
    OFF = 'off'
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    YELLOW = 'yellow'
    PURPLE = 'purple'
    CYAN = 'cyan'
    WHITE = 'white'
    ORANGE = 'orange'
    PINK = 'pink'

class LayerAction:
    """Special actions for layer management."""
    MODIFIER = 'modifier'   # Marks a key as the layer modifier


# =====================================================================================
# Keymap helpers
# =====================================================================================

# Store last-created structures so helper functions can expose useful info
_LAST_LAYERS = None
_LAST_CONFIG = None


def create_simple_keymap(keys, colors=None, name="Simple Keymap"):
    """
    Convert key definitions to the LAYERS format.

    Args:
        keys: dict of {position: keycode} where position is physical key number
        colors: dict of {position: color} (optional, defaults to blue)
        name: layer name

    Returns:
        tuple: (LAYERS, COLORS, CONFIG) dictionaries
    """

    # Default colors if not provided
    if colors is None:
        colors = {pos: Color.BLUE for pos in keys}

    # Convert position numbers to Key constants
    key_map = {}
    for pos, keycode in keys.items():
        # Find the Key constant that matches this position
        for attr_name in dir(Key):
            if not attr_name.startswith("R"):
                continue
            key_const = getattr(Key, attr_name)
            if key_const == pos:
                # If the provided key definition is a dict, pass it through (supports
                # modifier keys, dual-action keys, layer actions, etc.) and ensure a default color.
                if isinstance(keycode, dict):
                    value = dict(keycode)  # shallow copy
                    # Ensure colors/default present
                    value.setdefault("colors", {})
                    value["colors"].setdefault("default", colors.get(pos, Color.BLUE))
                    key_map[key_const] = value
                else:
                    # Key action (int keycode or list combo)
                    key_map[key_const] = {
                        "action_type": ActionType.KEY,
                        "action": keycode,
                        "colors": {"default": colors.get(pos, Color.BLUE)},
                    }
                break

    # Build LAYERS structure
    LAYERS = {
        0: {
            "name": name,
            "description": f"{name} layout",
            "color": Color.BLUE,
            "keys": key_map,
        }
    }

    # Build COLORS mapping (common colors)
    COLORS = {
        Color.OFF: (0, 0, 0),
        Color.WHITE: (255, 255, 255),
        Color.BLUE: (0, 0, 255),
        Color.GREEN: (0, 255, 0),
        Color.YELLOW: (255, 255, 0),
        Color.RED: (255, 0, 0),
        Color.ORANGE: (255, 128, 0),
        Color.PURPLE: (128, 0, 255),
        Color.CYAN: (0, 255, 255),
        Color.PINK: (255, 0, 128),
    }

    # Build CONFIG
    CONFIG = {
        "config_name": name,
        "config_description": f"{name} layout",
        "config_version": "1.0.0",
        "default_layer": 0,
        "brightness": 0.8,
        "led_sleep_enabled": True,
        "led_sleep_time": 30,
    }

    # Remember last generated values for helper access
    global _LAST_LAYERS, _LAST_CONFIG
    _LAST_LAYERS, _LAST_CONFIG = LAYERS, CONFIG

    return LAYERS, COLORS, CONFIG


def get_layer_name(layer: int) -> str:
    """Return the name of the given layer (fallback to numeric name)."""
    if isinstance(layer, int) and _LAST_LAYERS and layer in _LAST_LAYERS:
        return _LAST_LAYERS[layer].get("name", f"Layer {layer}")
    return f"Layer {layer}"


def get_config_info() -> dict:
    """Return a dictionary with config metadata expected by code.py."""
    layers = _LAST_LAYERS or {}
    config = _LAST_CONFIG or {}
    return {
        "name": config.get("config_name", "Simple configuration"),
        "version": config.get("config_version", ""),
        "layers": {i: v.get("name", str(i)) for i, v in layers.items()},
    }
