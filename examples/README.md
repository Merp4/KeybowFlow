# Example Configurations

7 ready-to-use layouts for the Pimoroni Keybow 2040. Each config is complete and self-contained.

## Quick Deployment

**Copy any config as your keymap:**

1. **Choose a configuration** from the list below
2. **Copy it to replace your keymap:**
   - Copy the config file over `src/keymap.py`
   - Copy `src/*.py` to your CIRCUITPY drive
3. **Your device will restart automatically**

**Examples:**

```bash
# Choose any configuration (examples shown)
cp examples/configs/numpad_minimal.py src/keymap.py
cp examples/configs/gaming_simple.py src/keymap.py  
cp examples/configs/productivity_simple.py src/keymap.py

# Copy to your device (CIRCUITPY drive)
cp src/*.py /path/to/CIRCUITPY/
```

**Or use the deployment script:**

```bash
python scripts/deploy.py numpad_minimal.py
```

## Available Configurations

### Single-Layer Layouts

- **[`numpad_minimal.py`](configs/numpad_minimal.py)** — Clean calculator-style numpad
- **[`gaming_simple.py`](configs/gaming_simple.py)** — WASD gaming keys and function keys
- **[`productivity_simple.py`](configs/productivity_simple.py)** — Common edit/navigation shortcuts
- **[`simple_numpad_lean.py`](configs/simple_numpad_lean.py)** — Alternative minimal numpad layout

### Multi-Layer Layouts

- **[`work_gaming_switch.py`](configs/work_gaming_switch.py)** — Dual-mode work/gaming switcher
- **[`streaming_setup.py`](configs/streaming_setup.py)** — Streaming controls and hotkeys  
- **[`developer_multitool.py`](configs/developer_multitool.py)** — Development environment with layers

## Making your own

All simple configs use the same pattern:

```python
from adafruit_hid.keycode import Keycode
from constants import Color, Key, create_simple_keymap, get_layer_name, get_config_info

# Define your keys: Key.RxCx -> keycode
keys = {
    Key.R0C0: Keycode.A, Key.R0C1: Keycode.B, Key.R0C2: Keycode.C, Key.R0C3: Keycode.D,
    # ... more keys
}

# Define colors: Key.RxCx -> color  
colors = {Key.R0C0: Color.RED, Key.R0C1: Color.GREEN, Key.R0C2: Color.BLUE, Key.R0C3: Color.YELLOW}

# Generate the full configuration
LAYERS, COLORS, CONFIG = create_simple_keymap(keys, colors, "My Layout")
```

For advanced configs with multiple layers, custom actions, etc., build your own `LAYERS`, `COLORS`, and `CONFIG` dictionaries directly using the patterns shown in the existing configs.

## Documentation

On-device documentation (available after installation):

- **docs/CONFIGURATION_GUIDE.md** — Step-by-step guide for creating custom configurations
- **docs/KEY_REFERENCE.md** — Complete list of all available keys and controls  
- **docs/ACTION_REFERENCE.md** — Action types and advanced features reference
- **docs/INSTALLATION.md** — Setup instructions and troubleshooting

## Layer System

Multi-layer configurations let you switch between different key layouts:

- **Layer 0**: Usually the main/default layer
- **Layer 1+**: Secondary layers for specialized functions
- **Layer switching**: Special keys that change the active layer

See the multi-layer configs above for examples of how this works in practice.
