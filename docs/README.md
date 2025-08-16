# KeybowFlow Documentation

Documentation for using and developing with KeybowFlow.

## User Guides

### [Installation Guide](INSTALLATION.md)

Installation instructions and quick start steps.

### [Configuration Guide](CONFIGURATION_GUIDE.md)

How to create and customize configurations, with examples and testing notes.

## Reference Documentation

### [Key Reference](KEY_REFERENCE.md)

Available keys, consumer control codes, modifiers, and examples.

### [Action Reference](ACTION_REFERENCE.md)

Action types, layer configuration, color themes, and action composition.

## Developer Guides

### [Development Guide](DEVELOPMENT.md)

Developer setup, test running, and contribution guidelines.

### [License Information](LICENSE.md)

Project and third-party license information.

## Project architecture

A high-level view of the repository layout:

```text
keybow/
├── src/                   # Core application
│   ├── code.py             # Main entry point
│   ├── keymap.py           # User key configuration
│   └── constants.py        # Hardware and layout constants
├── examples/               # Ready-to-use configs and layers
├── lib/                    # Vendored/submodule libraries (pmk)
├── scripts/                # Deployment and maintenance helpers
└── .github/                # CI/CD workflows
```

## Quick navigation

- New to Keybow? Start with the [Configuration Guide](CONFIGURATION_GUIDE.md).
- Want to customize? See the [Key Reference](KEY_REFERENCE.md) and examples in `examples/`.
- Contributing code? Read the [Development Guide](DEVELOPMENT.md).

## File formats

- `.md` — Markdown documentation files
- `.py` — Python/CircuitPython source code
- `.yml` — GitHub Actions workflow files

## External resources

- CircuitPython documentation: [https://docs.circuitpython.org/](https://docs.circuitpython.org/)
- PMK library: [https://github.com/pimoroni/pmk-circuitpython](https://github.com/pimoroni/pmk-circuitpython)
- Adafruit CircuitPython bundle: [https://github.com/adafruit/Adafruit_CircuitPython_Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle)

---

Documentation last updated: August 2025
