# Installation

This document explains how to install a release build of KeybowFlow onto a Keybow 2040 device (CIRCUITPY).

## Before you begin

### Firmware download

Keybow 2040 firmware builds (official): https://circuitpython.org/board/pimoroni_keybow2040/

A compatible UF2 firmware file is also included in the project releases for convenience and compatibility. If you encounter issues with the official firmware, use the UF2 provided in the release artifacts.

## Install release artifacts

1. Download the release artifact (for example, `keybow-device-files.zip`) from the project's releases page.
2. Extract the archive to a temporary folder.
3. Copy the extracted runtime files to the device root. On Windows PowerShell:

```powershell
# replace <CIRCUITPY> with the actual mount point, for example E:\
Copy-Item -Path <extracted_path>\* -Destination <CIRCUITPY>\ -Recurse -Force
```

After copying, the device should contain the runtime files (for example `code.py`, `keymap.py`, `constants.py`) and a `lib/` directory with required CircuitPython libraries.

## Installing device libraries

Release artifacts typically include a populated `lib/` directory with the required CircuitPython libraries. If a release does not include `lib/`, install libraries listed in `cp_requirements.txt` using `circup` from a host environment:

```powershell
circup install -r cp_requirements.txt
```

This downloads and installs libraries directly onto the connected device. Only run `circup` when the device is connected and mounted.

## Verifying the install

- Confirm `code.py` (or `main.py`) and `keymap.py` are present on the CIRCUITPY root.
- Confirm `lib/` contains required libraries referenced by the runtime files.
- If available, open a serial console to view device logs for errors and startup messages.

## Troubleshooting

- Device not detected: try a different USB cable or port and verify a `CIRCUITPY` volume appears.
- Missing libraries: ensure `lib/` on the device contains the required CircuitPython packages; if not, use `circup`.
- Code not running: check for syntax errors and missing imports; use a development environment to reproduce and test if needed.

## Development and source installs

For installing from source or setting up a development environment (virtualenv, tooling, running tests), see `docs/DEVELOPMENT.md`.
