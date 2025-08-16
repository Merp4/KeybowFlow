# Configuration Guide

Guide for creating custom Keybow 2040 configurations.

## Quick Start

### 1. Choose a Template

Start with a configuration that matches your needs:

- ultra_simple_numpad.py - Basic 16-key numpad
- productivity_simple.py - Text editing shortcuts  
- gaming_simple.py - Gaming macros and controls
- work_gaming_switch.py - Multi-layer work/gaming toggle

### 2. Copy and Rename

```bash
cp examples/configs/ultra_simple_numpad.py my_config.py
```

### 3. Basic Customization

Edit the key mappings in your new file:

```python
from constants import create_simple_keymap, Color

# Simple approach - just list what each key should do
KEYMAP = create_simple_keymap([
    # Row 3 (top)
    'F9', 'F10', 'F11', 'F12',
    # Row 2  
    'F5', 'F6', 'F7', 'F8',
    # Row 1
    'F1', 'F2', 'F3', 'F4',
    # Row 0 (bottom)
    'ESC', 'TAB', 'ENTER', 'SPACE'
])
```

## Configuration Structure

### Basic Configuration File

Every configuration needs these components:

```python
from constants import create_simple_keymap, Color

# 1. Key mappings
KEYMAP = create_simple_keymap([...])

# 2. Color definitions
COLORS = {
    Color.BLUE: (0, 100, 255),
    Color.RED: (255, 50, 50)
}

# 3. Configuration metadata
CONFIG = {
    'config_name': 'My Custom Layout',
    'config_description': 'Brief description',
    'config_version': '1.0.0',
    'brightness': 0.8
}
```

### Multi-Layer Configuration File

For more complex setups with multiple layers:

```python
from constants import ActionType, Key, Color

# 1. Layer definitions
LAYERS = {
    0: {  # Main layer
        'name': 'Primary',
        'keys': { Key.R0C0: {...}, ... }
    },
    1: {  # Secondary layer  
        'name': 'Secondary', 
        'keys': { Key.R0C0: {...}, ... }
    }
}

# 2. Colors and config same as basic
```

## Common Key Patterns

### Text Shortcuts

```python
# Copy, Cut, Paste, Undo
['CTRL+C', 'CTRL+X', 'CTRL+V', 'CTRL+Z']

# Text navigation
['HOME', 'END', 'PAGE_UP', 'PAGE_DOWN']

# Text selection
['CTRL+A', 'CTRL+SHIFT+LEFT', 'CTRL+SHIFT+RIGHT', 'SHIFT+END']
```

### Media Controls

```python
# Basic media
['PLAY_PAUSE', 'VOLUME_MUTE', 'VOLUME_DECREMENT', 'VOLUME_INCREMENT']

# Extended media
['SCAN_PREVIOUS_TRACK', 'SCAN_NEXT_TRACK', 'STOP', 'EJECT']
```

### Function Keys

```python
# Standard F-keys
['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8']

# Extended F-keys  
['F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16']
```

### Number Pad

```python
# Classic numpad layout
[
    'KEYPAD_NUMLOCK', 'KEYPAD_FORWARD_SLASH', 'KEYPAD_ASTERISK', 'KEYPAD_MINUS',
    'KEYPAD_SEVEN', 'KEYPAD_EIGHT', 'KEYPAD_NINE', 'KEYPAD_PLUS', 
    'KEYPAD_FOUR', 'KEYPAD_FIVE', 'KEYPAD_SIX', 'KEYPAD_PLUS',
    'KEYPAD_ONE', 'KEYPAD_TWO', 'KEYPAD_THREE', 'KEYPAD_ENTER'
]
```

## Color Schemes

### Standard Theme

```python
COLORS = {
    Color.BLUE: (0, 50, 150),      # Primary actions
    Color.GREEN: (0, 150, 50),     # Positive actions  
    Color.RED: (150, 50, 0),       # Warning actions
    Color.YELLOW: (150, 150, 0),   # Secondary actions
    Color.WHITE: (100, 100, 100),  # Neutral actions
    Color.OFF: (0, 0, 0)           # Disabled keys
}
```

### Gaming Theme

```python
COLORS = {
    Color.RED: (255, 0, 0),        # Combat/action
    Color.BLUE: (0, 0, 255),       # Movement/navigation
    Color.GREEN: (0, 255, 0),      # Inventory/items
    Color.PURPLE: (255, 0, 255),   # Special abilities
    Color.YELLOW: (255, 255, 0),   # Communication
    Color.CYAN: (0, 255, 255)      # System/settings
}
```

### Minimal Theme

```python
COLORS = {
    Color.WHITE: (50, 50, 50),     # All keys same dim white
    Color.BLUE: (0, 50, 100),      # Accent for special keys
    Color.OFF: (0, 0, 0)           # Disabled
}
```

## Advanced Features

### Custom Text Strings

```python
# For frequent text
KEYMAP = create_simple_keymap([
    'user@company.com',     # Email
    'https://example.com',  # URL
    '+1-555-123-4567',     # Phone
    'John Doe'             # Name
])
```

### Application Shortcuts

```python
# Launch applications
['GUI+R|notepad',          # Windows: Run dialog + notepad
 'GUI+R|calc',             # Calculator
 'GUI+R|cmd',              # Command prompt
 'CTRL+SHIFT+ESC']         # Task manager
```

### Development Shortcuts

```python
# Code editing
['CTRL+SHIFT+P',           # Command palette
 'CTRL+SHIFT+F',           # Find in files
 'CTRL+SHIFT+T',           # Reopen closed tab
 'F5']                     # Debug/run
```

## Testing Your Configuration

### 1. Syntax Check

Save your file and check for Python syntax errors:

```python
# Make sure imports work
from constants import create_simple_keymap, Color

# Verify your keymap is valid
print(len(KEYMAP))  # Should be 16 for full keypad
```

### 2. Deploy and Test

Copy to your Keybow 2040:

```bash
# Copy your configuration
cp my_config.py /path/to/keybow/code.py

# Test individual keys gradually
# Start with safe keys like F1, F2, etc.
```

### 3. Common Issues

**Keys not responding:**
- Check USB connection
- Verify key names match reference docs
- Ensure proper syntax in configuration

**Wrong characters:**
- Check keyboard layout settings
- Verify modifier key combinations
- Test with simple keys first

**LEDs not lighting:**
- Check brightness setting
- Verify color definitions
- Ensure power is sufficient

## Guidelines

### Start Simple

Begin with basic key mappings before adding complex features:

```python
# Good: Start with this
KEYMAP = create_simple_keymap(['A', 'B', 'C', 'D', ...])

# Later: Add complexity
LAYERS = { 0: {...}, 1: {...} }
```

### Logical Grouping

Organize keys by function:

```python
# Row 3: Media controls
['PLAY_PAUSE', 'VOLUME_MUTE', 'VOLUME_DECREMENT', 'VOLUME_INCREMENT']

# Row 2: Text editing
['CTRL+C', 'CTRL+X', 'CTRL+V', 'CTRL+Z']

# Row 1: Navigation
['HOME', 'END', 'PAGE_UP', 'PAGE_DOWN']

# Row 0: Special functions
['ESC', 'TAB', 'ENTER', 'SPACE']
```

### Color Consistency

Use colors to indicate function groups:

```python
# Blue for media
# Green for text editing  
# Red for system/dangerous actions
# Yellow for navigation
```

### Documentation

Comment your configuration:

```python
CONFIG = {
    'config_name': 'Video Editing Setup',
    'config_description': 'Optimized for Adobe Premiere Pro workflow',
    'config_version': '1.2.0'
}

# Shortcuts for timeline navigation
KEYMAP = create_simple_keymap([
    'J',           # Reverse play
    'K',           # Pause
    'L',           # Forward play
    'SPACE',       # Play/pause toggle
    # ... more keys
])
```

## Troubleshooting

### Configuration Not Loading

1. Check file syntax
2. Verify all imports
3. Ensure file is named correctly
4. Check for missing commas/brackets

### Keys Not Working

1. Test with simple keys (A, B, C)
2. Check key name spelling
3. Verify modifier combinations
4. Test one key at a time

### LED Issues

1. Check brightness setting (0.0 to 1.0)
2. Verify color definitions
3. Test with basic colors first
4. Check power supply

### Getting Help

- Check example configurations for patterns
- Reference KEY_REFERENCE.md for available keys
- Reference ACTION_REFERENCE.md for advanced features
- Test incrementally with simple configurations
