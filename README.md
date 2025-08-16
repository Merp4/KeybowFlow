# KeybowFlow

A configuration framework for the Pimoroni Keybow 2040 with support for multiple layers, customizable LED themes, and various input actions.

## 🚀 Quick Start

1. Download the latest `keybowflow-device-files.zip` from [Releases](https://github.com/Merp4/KeybowFlow/releases)
2. Extract all files to your Keybow 2040 (CIRCUITPY drive)
3. Edit `keymap.py` to customize your keys

## 📋 Example Configurations

- [`numpad_minimal.py`](examples/configs/numpad_minimal.py) - Calculator-style numpad  
- [`gaming_simple.py`](examples/configs/gaming_simple.py) - WASD gaming keys and function keys
- [`productivity_simple.py`](examples/configs/productivity_simple.py) - Common edit/navigation shortcuts
- [`work_gaming_switch.py`](examples/configs/work_gaming_switch.py) - Dual-mode work/gaming switcher
- [`streaming_setup.py`](examples/configs/streaming_setup.py) - Streaming controls and hotkeys
- [`developer_multitool.py`](examples/configs/developer_multitool.py) - Development environment with layers

## ⚡ Quick Config Example

```python
# Simple 4-key layout
from adafruit_hid.keycode import Keycode
from constants import Color, Key, create_simple_keymap

keys = {
    Key.R0C0: Keycode.A,           # Top-left
    Key.R0C1: Keycode.B,           # Top-right  
    Key.R1C0: [Keycode.CTRL, Keycode.C],  # Second row left (Ctrl+C)
    Key.R1C1: "Hello World!"       # Second row right (types text)
}

colors = {Key.R0C0: Color.BLUE, Key.R0C1: Color.GREEN, Key.R1C0: Color.RED, Key.R1C1: Color.YELLOW}
LAYERS, COLORS, CONFIG = create_simple_keymap(keys, colors, "My Layout")
```

Copy this as `keymap.py` to your device and customize!

## 📚 Documentation

- [Configuration Guide](docs/CONFIGURATION_GUIDE.md) - Create custom keymaps and layers
- [Key Reference](docs/KEY_REFERENCE.md) - Available keys and controls
- [Action Reference](docs/ACTION_REFERENCE.md) - Action types and features
- [Development Guide](docs/DEVELOPMENT.md) - Contributing and building from source
- [Installation Guide](docs/INSTALLATION.md) - Setup instructions and troubleshooting

## Requirements

- **Hardware**: Pimoroni Keybow 2040
- **Firmware**: CircuitPython 9.2.8+
- **Development**: Python 3.13+ (for modifications)

## Credits

KeybowFlow is built on the excellent [PMK (Pimoroni Mechanical/Mushy Keypad) library](https://github.com/pimoroni/pmk-circuitpython) by Pimoroni. The multi-layer configuration system is inspired by the [`hid-keypad-fifteen-layers.py`](lib/pmk/examples/hid-keypad-fifteen-layers.py) example by Sandy Macdonald.

## Additional Information

- [Changelog](CHANGELOG.md) - Version history and release notes
- [Third-Party Licenses](docs/THIRD_PARTY_LICENSES.md) - License information for included libraries
