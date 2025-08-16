# Key Reference

Reference for all available keys and controls that can be used in Keybow 2040 configurations.

## Standard Keyboard Keys

### Letters
```python
Keycode.A, Keycode.B, Keycode.C, Keycode.D, Keycode.E, Keycode.F, Keycode.G, Keycode.H, 
Keycode.I, Keycode.J, Keycode.K, Keycode.L, Keycode.M, Keycode.N, Keycode.O, Keycode.P, 
Keycode.Q, Keycode.R, Keycode.S, Keycode.T, Keycode.U, Keycode.V, Keycode.W, Keycode.X, 
Keycode.Y, Keycode.Z
```

### Numbers
```python
Keycode.ONE, Keycode.TWO, Keycode.THREE, Keycode.FOUR, Keycode.FIVE, 
Keycode.SIX, Keycode.SEVEN, Keycode.EIGHT, Keycode.NINE, Keycode.ZERO
```

### Function Keys
```python
Keycode.F1, Keycode.F2, Keycode.F3, Keycode.F4, Keycode.F5, Keycode.F6, 
Keycode.F7, Keycode.F8, Keycode.F9, Keycode.F10, Keycode.F11, Keycode.F12, 
Keycode.F13, Keycode.F14, Keycode.F15, Keycode.F16, Keycode.F17, Keycode.F18, 
Keycode.F19, Keycode.F20, Keycode.F21, Keycode.F22, Keycode.F23, Keycode.F24
```

### Modifier Keys
```python
Keycode.CONTROL        # Ctrl key
Keycode.SHIFT          # Shift key
Keycode.ALT            # Alt key
Keycode.GUI            # Windows/Cmd key
Keycode.LEFT_CONTROL   # Left Ctrl
Keycode.LEFT_SHIFT     # Left Shift
Keycode.LEFT_ALT       # Left Alt
Keycode.LEFT_GUI       # Left Windows/Cmd
Keycode.RIGHT_CONTROL  # Right Ctrl
Keycode.RIGHT_SHIFT    # Right Shift
Keycode.RIGHT_ALT      # Right Alt (AltGr)
Keycode.RIGHT_GUI      # Right Windows/Cmd
```

### Arrow Keys
```python
Keycode.UP_ARROW       # ↑
Keycode.DOWN_ARROW     # ↓
Keycode.LEFT_ARROW     # ←
Keycode.RIGHT_ARROW    # →
```

### Navigation Keys
```python
Keycode.PAGE_UP        # Page Up
Keycode.PAGE_DOWN      # Page Down
Keycode.HOME           # Home
Keycode.END            # End
Keycode.INSERT         # Insert
Keycode.DELETE         # Delete
```

### Special Keys
```python
Keycode.ENTER          # Enter/Return
Keycode.ESCAPE         # Escape
Keycode.BACKSPACE      # Backspace
Keycode.TAB            # Tab
Keycode.SPACE          # Space
Keycode.CAPS_LOCK      # Caps Lock
Keycode.PRINT_SCREEN   # Print Screen
Keycode.SCROLL_LOCK    # Scroll Lock
Keycode.PAUSE          # Pause/Break
Keycode.APPLICATION    # Menu key
```

### Punctuation and Symbols
```python
Keycode.MINUS          # - (hyphen)
Keycode.EQUALS         # = (equals)
Keycode.LEFT_BRACKET   # [ (left bracket)
Keycode.RIGHT_BRACKET  # ] (right bracket)
Keycode.BACKSLASH      # \ (backslash)
Keycode.SEMICOLON      # ; (semicolon)
Keycode.QUOTE          # ' (apostrophe)
Keycode.GRAVE_ACCENT   # ` (grave accent/backtick)
Keycode.COMMA          # , (comma)
Keycode.PERIOD         # . (period)
Keycode.FORWARD_SLASH  # / (forward slash)
```

### Keypad (Numeric)
```python
Keycode.KEYPAD_NUMLOCK       # Num Lock
Keycode.KEYPAD_FORWARD_SLASH # Keypad /
Keycode.KEYPAD_ASTERISK      # Keypad *
Keycode.KEYPAD_MINUS         # Keypad -
Keycode.KEYPAD_PLUS          # Keypad +
Keycode.KEYPAD_ENTER         # Keypad Enter
Keycode.KEYPAD_ONE           # Keypad 1
Keycode.KEYPAD_TWO           # Keypad 2
Keycode.KEYPAD_THREE         # Keypad 3
Keycode.KEYPAD_FOUR          # Keypad 4
Keycode.KEYPAD_FIVE          # Keypad 5
Keycode.KEYPAD_SIX           # Keypad 6
Keycode.KEYPAD_SEVEN         # Keypad 7
Keycode.KEYPAD_EIGHT         # Keypad 8
Keycode.KEYPAD_NINE          # Keypad 9
Keycode.KEYPAD_ZERO          # Keypad 0
Keycode.KEYPAD_PERIOD        # Keypad .
```

## Consumer Control Codes

Consumer controls are used for media keys and system functions. Import with:
```python
from adafruit_hid.consumer_control_code import ConsumerControlCode
```

### Media Controls
```python
ConsumerControlCode.PLAY_PAUSE          # Play/Pause media
ConsumerControlCode.STOP                # Stop media
ConsumerControlCode.SCAN_NEXT_TRACK     # Next track
ConsumerControlCode.SCAN_PREVIOUS_TRACK # Previous track
ConsumerControlCode.FAST_FORWARD        # Fast forward
ConsumerControlCode.REWIND              # Rewind
ConsumerControlCode.RECORD              # Record
ConsumerControlCode.EJECT               # Eject media
```

### Volume Controls
```python
ConsumerControlCode.VOLUME_INCREMENT    # Volume up
ConsumerControlCode.VOLUME_DECREMENT    # Volume down
ConsumerControlCode.MUTE                # Mute/unmute
```

### Browser Controls
```python
ConsumerControlCode.AC_BACK             # Browser back
ConsumerControlCode.AC_FORWARD          # Browser forward
ConsumerControlCode.AC_REFRESH          # Browser refresh
ConsumerControlCode.AC_STOP             # Browser stop
ConsumerControlCode.AC_SEARCH           # Browser search
ConsumerControlCode.AC_BOOKMARKS        # Browser bookmarks
ConsumerControlCode.AC_HOME             # Browser home
```

### Application Controls
```python
ConsumerControlCode.CALCULATOR          # Open calculator
ConsumerControlCode.EMAIL               # Open email
ConsumerControlCode.BROWSER             # Open browser
ConsumerControlCode.CONSUMER_CONTROL    # Generic consumer control
```

### Power Controls
```python
ConsumerControlCode.POWER               # Power button
ConsumerControlCode.SLEEP               # Sleep
```

## Key Combinations

Use lists for key combinations (modifier + key):

```python
# Examples
[Keycode.CONTROL, Keycode.C]           # Ctrl+C (copy)
[Keycode.CONTROL, Keycode.V]           # Ctrl+V (paste)
[Keycode.CONTROL, Keycode.Z]           # Ctrl+Z (undo)
[Keycode.CONTROL, Keycode.SHIFT, Keycode.Z]  # Ctrl+Shift+Z (redo)
[Keycode.ALT, Keycode.TAB]             # Alt+Tab (window switch)
[Keycode.GUI, Keycode.L]               # Windows+L (lock screen)
[Keycode.CONTROL, Keycode.ALT, Keycode.DELETE]  # Ctrl+Alt+Del
```

## Usage Examples

### In Configuration Files
```python
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from constants import ActionType

# Keyboard keys
Key.R0C0: {
    'action_type': ActionType.KEY,
    'action': Keycode.A,
    'colors': {'default': Color.BLUE}
}

# Key combinations
Key.R0C1: {
    'action_type': ActionType.KEY,
    'action': [Keycode.CONTROL, Keycode.C],
    'colors': {'default': Color.GREEN}
}

# Consumer controls
Key.R0C2: {
    'action_type': ActionType.CONSUMER,
    'action': ConsumerControlCode.PLAY_PAUSE,
    'colors': {'default': Color.PURPLE}
}

# Text strings
Key.R0C3: {
    'action_type': ActionType.STRING,
    'action': "Hello, World!",
    'colors': {'default': Color.YELLOW}
}
```

### Common Shortcuts
```python
# Text editing
[Keycode.CONTROL, Keycode.A]           # Select all
[Keycode.CONTROL, Keycode.X]           # Cut
[Keycode.CONTROL, Keycode.C]           # Copy
[Keycode.CONTROL, Keycode.V]           # Paste
[Keycode.CONTROL, Keycode.Z]           # Undo
[Keycode.CONTROL, Keycode.Y]           # Redo
[Keycode.CONTROL, Keycode.F]           # Find
[Keycode.CONTROL, Keycode.H]           # Replace
[Keycode.CONTROL, Keycode.S]           # Save

# File operations
[Keycode.CONTROL, Keycode.N]           # New file
[Keycode.CONTROL, Keycode.O]           # Open file
[Keycode.CONTROL, Keycode.W]           # Close tab/window
[Keycode.CONTROL, Keycode.SHIFT, Keycode.T]  # Reopen closed tab

# Navigation
[Keycode.ALT, Keycode.LEFT_ARROW]      # Back
[Keycode.ALT, Keycode.RIGHT_ARROW]     # Forward
[Keycode.CONTROL, Keycode.TAB]         # Next tab
[Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]  # Previous tab

# System
[Keycode.ALT, Keycode.F4]              # Close application
[Keycode.GUI, Keycode.D]               # Show desktop
[Keycode.GUI, Keycode.R]               # Run dialog
[Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE]  # Task manager
```

## Notes

- **Key combinations** are executed as simultaneous key presses
- **Consumer controls** work with media applications and system volume
- **Modifier keys** (Ctrl, Shift, Alt, GUI) are typically used in combinations
- **String actions** type text directly (useful for email addresses, URLs, etc.)
- Some keys may not work on all operating systems or applications
- Test key combinations in your target applications to ensure compatibility
