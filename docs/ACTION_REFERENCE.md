# Action Types Reference

Reference for all action types and advanced features available in Keybow 2040 configurations.

## Action Types

### ActionType.KEY
Execute keyboard key presses and combinations.

```python
from adafruit_hid.keycode import Keycode
from constants import ActionType

# Single key
{
    'action_type': ActionType.KEY,
    'action': Keycode.A,
    'colors': {'default': Color.BLUE}
}

# Key combination
{
    'action_type': ActionType.KEY,
    'action': [Keycode.CONTROL, Keycode.C],
    'colors': {'default': Color.GREEN}
}
```

### ActionType.STRING
Type text strings directly.

```python
{
    'action_type': ActionType.STRING,
    'action': "Hello, World!",
    'colors': {'default': Color.YELLOW}
}

# Common use cases
{
    'action_type': ActionType.STRING,
    'action': "user@example.com",  # Email addresses
    'colors': {'default': Color.CYAN}
}

{
    'action_type': ActionType.STRING,
    'action': "https://example.com",  # URLs
    'colors': {'default': Color.BLUE}
}
```

### ActionType.CONSUMER
Media and system controls.

```python
from adafruit_hid.consumer_control_code import ConsumerControlCode

{
    'action_type': ActionType.CONSUMER,
    'action': ConsumerControlCode.PLAY_PAUSE,
    'colors': {'default': Color.PURPLE}
}

{
    'action_type': ActionType.CONSUMER,
    'action': ConsumerControlCode.VOLUME_INCREMENT,
    'colors': {'default': Color.GREEN}
}
```

### ActionType.SEQUENCE
Execute multiple actions in order.

```python
{
    'action_type': ActionType.SEQUENCE,
    'action': [
        {'type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.A]},
        {'type': ActionType.KEY, 'action': [Keycode.CONTROL, Keycode.C]},
        {'type': ActionType.STRING, 'action': "Copied all text"}
    ],
    'colors': {'default': Color.ORANGE}
}
```

### ActionType.LAYER
Switch between configuration layers.

```python
{
    'action_type': ActionType.LAYER,
    'action': 1,  # Switch to layer 1
    'colors': {'default': Color.WHITE}
}

# Special layer actions
from constants import LayerAction

{
    'action_type': ActionType.LAYER,
    'action': LayerAction.MODIFIER,  # Modifier key behavior
    'colors': {'default': Color.WHITE}
}
```

### ActionType.FUNCTION
Execute custom Python functions.

```python
def toggle_led_brightness():
    # Custom function implementation
    pass

{
    'action_type': ActionType.FUNCTION,
    'action': toggle_led_brightness,
    'colors': {'default': Color.PINK}
}
```

## Color Configuration

### Basic Colors
```python
from constants import Color

'colors': {'default': Color.RED}
'colors': {'default': Color.GREEN}
'colors': {'default': Color.BLUE}
'colors': {'default': Color.YELLOW}
'colors': {'default': Color.PURPLE}
'colors': {'default': Color.CYAN}
'colors': {'default': Color.WHITE}
'colors': {'default': Color.OFF}
```

### State-Based Colors
```python
'colors': {
    'default': Color.BLUE,      # Normal state
    'pressed': Color.WHITE,     # When key is pressed
    'active': Color.GREEN       # When feature is active
}
```

### Custom RGB Colors
```python
# Define custom colors in COLORS dictionary
COLORS = {
    Color.CUSTOM_ORANGE: (255, 128, 0),
    Color.CUSTOM_PINK: (255, 192, 203),
    Color.CUSTOM_LIME: (50, 205, 50)
}

# Use in configuration
'colors': {'default': Color.CUSTOM_ORANGE}
```

## Layer Configuration

### Basic Layer Setup
```python
LAYERS = {
    0: {  # Layer 0 (default)
        'name': 'Main Layer',
        'description': 'Primary functions',
        'color': Color.BLUE,
        'keys': {
            # Key configurations here
        }
    },
    1: {  # Layer 1
        'name': 'Secondary Layer',
        'description': 'Alternative functions',
        'color': Color.RED,
        'keys': {
            # Different key configurations
        }
    }
}
```

### Layer Switching
```python
# Modifier key pattern (hold to access layer)
Key.R3C0: {
    'action_type': ActionType.LAYER,
    'action': LayerAction.MODIFIER,
    'colors': {'default': Color.WHITE, 'pressed': Color.BLUE}
}

# Direct layer switch (toggle to layer)
Key.R0C0: {
    'action_type': ActionType.LAYER,
    'action': 1,  # Switch to layer 1
    'colors': {'default': Color.RED}
}
```

## Advanced Features

### Brightness Control
```python
CONFIG = {
    'brightness': 0.8,  # 80% brightness (0.0 to 1.0)
    'led_sleep_enabled': True,
    'led_sleep_time': 300  # 5 minutes
}
```

### Configuration Metadata
```python
CONFIG = {
    'config_name': 'My Custom Layout',
    'config_description': 'Description of what this layout does',
    'config_version': '1.0.0',
    'default_layer': 0,
    'modifier_key': Key.R3C0  # Bottom-left key as modifier
}
```

## Key Position Reference

Physical layout positions for 4x4 Keybow 2040:

```text
Physical:    Constants:
[ 3][ 7][11][15]    [R0C0][R0C1][R0C2][R0C3]
[ 2][ 6][10][14]    [R1C0][R1C1][R1C2][R1C3]  
[ 1][ 5][ 9][13]    [R2C0][R2C1][R2C2][R2C3]
[ 0][ 4][ 8][12]    [R3C0][R3C1][R3C2][R3C3]
```

### Key Constants
```python
from constants import Key

# Top row (R0)
Key.R0C0, Key.R0C1, Key.R0C2, Key.R0C3

# Second row (R1)  
Key.R1C0, Key.R1C1, Key.R1C2, Key.R1C3

# Third row (R2)
Key.R2C0, Key.R2C1, Key.R2C2, Key.R2C3

# Bottom row (R3)
Key.R3C0, Key.R3C1, Key.R3C2, Key.R3C3
```

## Complete Example

```python
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from constants import ActionType, Key, Color, LayerAction

LAYERS = {
    0: {
        'name': 'Main',
        'description': 'Primary functions',
        'color': Color.BLUE,
        'keys': {
            Key.R0C0: {
                'action_type': ActionType.KEY,
                'action': Keycode.A,
                'colors': {'default': Color.BLUE, 'pressed': Color.WHITE}
            },
            Key.R0C1: {
                'action_type': ActionType.STRING,
                'action': "Hello!",
                'colors': {'default': Color.GREEN}
            },
            Key.R0C2: {
                'action_type': ActionType.CONSUMER,
                'action': ConsumerControlCode.PLAY_PAUSE,
                'colors': {'default': Color.PURPLE}
            },
            Key.R0C3: {
                'action_type': ActionType.LAYER,
                'action': 1,
                'colors': {'default': Color.RED}
            }
        }
    }
}

COLORS = {
    Color.BLUE: (0, 100, 255),
    Color.GREEN: (0, 255, 100),
    Color.RED: (255, 50, 50),
    Color.PURPLE: (128, 0, 255),
    Color.WHITE: (255, 255, 255)
}

CONFIG = {
    'config_name': 'Example Configuration',
    'config_description': 'Demonstrates all action types',
    'config_version': '1.0.0',
    'default_layer': 0,
    'brightness': 0.8,
    'led_sleep_enabled': True,
    'led_sleep_time': 300
}
```

## Notes

- Test incrementally: start with simple actions before adding complex sequences.
- Use descriptive layer names to aid debugging.
- Use consistent color themes to indicate function groups.
- Common modifier: bottom-left key (R3C0) for layer switching.
- Lower brightness reduces power use and extends LED life.
- Enable sleep timers to save power when idle.
