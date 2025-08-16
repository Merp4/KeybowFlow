# Installation Guide

## Setup

1. Download `keybow-device-files.zip` from the project's releases.
2. Extract the files to your Keybow 2040 device (appears as the CIRCUITPY drive when connected).
3. Edit `keymap.py` to customize key behavior.
4. The device restarts after copying files.

## Development Setup

For development from source code:

1. **Copy files manually**:

   ```bash
   # Copy source files to your CIRCUITPY drive
   cp src/*.py /path/to/CIRCUITPY/
   cp -r lib/* /path/to/CIRCUITPY/lib/
   ```

2. **Or use deployment script**:

   ```bash
   python scripts/deploy.py numpad_minimal.py
   ```

## CircuitPython Firmware

Download CircuitPython firmware for Keybow 2040 from:

- <https://downloads.circuitpython.org/bin/pimoroni_keybow2040/>

## Customization

- Extract `keybow-examples.zip` for configurations
- Copy any example config over existing files
- See `README.md` for customization instructions

## Troubleshooting

- **Device not appearing**: Try different USB cable or port
- **Code not working**: Check for syntax errors in `keymap.py`
- **Missing features**: Ensure all files from ZIP are copied

See the README.md for additional information.

## File Structure After Installation

Once installed, your CIRCUITPY drive should contain:

```text
CIRCUITPY/
├── code.py              # Main application entry point
├── keymap.py            # Your key configuration
├── constants.py         # System constants and layout
├── lib/                 # Libraries directory
│   ├── pmk/            # PMK library (Pimoroni)
│   ├── adafruit_hid/   # HID library
│   ├── adafruit_bus_device/
│   └── adafruit_is31fl3731/
├── examples/           # Example configurations
│   ├── configs/        # Pre-built key layouts
│   └── README.md
├── scripts/            # Setup and deployment scripts
└── README.md           # Main documentation
```

## Version Information

- **CircuitPython**: 9.2.8 or later
- **PMK library**: provided as a git submodule under `lib/pmk`
- **Adafruit libraries**: managed via CircUp and `cp_requirements.txt`
   - Run `circup install -r cp_requirements.txt` from the project root to install all required libraries with pinned versions.

## Getting Help

- **Documentation**: Check `docs/` directory for detailed guides
- **Examples**: Look in `examples/configs/` for pre-built configurations
- **Issues**: Report problems at the project repository
- **Community**: CircuitPython community forums and Discord
