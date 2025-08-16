# Development Guide

Advanced development workflow and debugging for the Keybow 2040.

## Development Workflow

### Standard development

1. Edit configuration (modify `keymap.py` or create a new config).
2. Deploy files to the CIRCUITPY drive (manual or using `scripts/deploy.py`).
3. Monitor serial output for debugging.

### Custom configuration

Start from an example in `examples/configs/`, edit it, and deploy using `scripts/deploy.py`.


## Serial Monitoring

### Serial monitoring

Use a serial terminal to monitor the device output. On Unix-like systems `screen` or `picocom` are common; on Windows use a serial terminal application. Replace the device path/port as appropriate for your system.


## Debug Output

Example debug output:

Configuration loaded from keymap.py
Starting layer: 0 (Main)
Layer switch: Main -> VS Code
Key 12 pressed - Layer: VS Code


## Common Issues

### Import Errors

- Copy files manually: `cp src/*.py /path/to/CIRCUITPY/` (simpler than scripts)
- Check `lib/` folder has all libraries

If `lib/pmk` is missing (PMK library submodule), run:

```bash
git submodule update --init --recursive
```


### Device Not Found

- Check USB connection
- Verify CircuitPython installation
- Try different USB port


### Configuration Errors

- Check keymap.py syntax
- Verify all required imports
- Use examples as reference


## Project structure

```text
Keybow/
├── src/                    # Core CircuitPython source files
├── examples/               # Ready-to-use configurations
├── docs/                   # Documentation
├── lib/                    # Vendored/submodule libraries (pmk)
└── .github/                # CI/CD workflows
```


## Advanced Features

### Multiple Configurations

Keep multiple configs for different use cases:

```bash
# Gaming
python scripts/deploy.py gaming_simple.py

# Work
python scripts/deploy.py productivity_simple.py
```

### Real-time Development

1. Edit configuration in your editor
2. Deploy instantly with script
3. Monitor changes via serial
4. Iterate quickly

## Developer helper scripts

Note: `requirements.txt` is the repository's source of truth for pinned Python tooling used by development and CI (for example `circup`). Workflows are configured to install from `requirements.txt` so updating that file is the normal way to update CI and local tooling.
