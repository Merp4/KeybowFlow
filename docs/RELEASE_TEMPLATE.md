# Keybow 2040 Release Template

## Keybow 2040 Release {version}

### Quick Installation

1. Download `keybow-device-files.zip`
2. Extract to your Keybow 2040 CIRCUITPY drive
3. Edit `keymap.py` to customize

### Files Included

- **keybow-device-files.zip**: Complete project ready for device
- **keybow-examples.zip**: Example configurations  
- **circuitpython-keybow2040-{firmware_version}.uf2**: CircuitPython {firmware_version} firmware
- **INSTALLATION.md**: Detailed setup instructions
- **CONFIGURATION_GUIDE.md**: Create custom keymaps and layers
- **KEY_REFERENCE.md**: All available keys and controls  
- **ACTION_REFERENCE.md**: Action types and advanced features
- **CHANGELOG.md**: Version history and changes
- **THIRD_PARTY_LICENSES.md**: License information for included libraries
- **LICENSE.txt**: Main project license (MIT)

### System Requirements

- **Hardware**: Pimoroni Keybow 2040
- **Firmware**: CircuitPython {firmware_version} or later
- **Storage**: ~2MB free space on device
- **Development**: Python 3.13+ (for modifications)

### What's New

{changelog}

### Compatibility Notes

- **Firmware**: Compatible with CircuitPython {firmware_version}+
- **Operating Systems**: Windows, macOS, Linux  
- **Development Tools**: VS Code, Thonny, or any text editor
- **Previous Versions**: See INSTALLATION.md for migration guidance

### Quick Links

- 📖 **Installation**: See included INSTALLATION.md
- 🎮 **Examples**: Extract keybow-examples.zip for pre-built configs
- 🛠️ **Customization**: Edit keymap.py to modify key behaviors
- 🐛 **Issues**: Report problems at project repository

---

**Build Information:**

- Version: {version}
- CircuitPython: {firmware_version}
- Build Commit: {commit_sha}
- Dependencies: See .github/workflows/ for current versions

### License Information

This project is released under the MIT License. All included third-party libraries (Adafruit CircuitPython libraries, PMK) are also MIT licensed. See THIRD_PARTY_LICENSES.md for complete attribution and license details.

*For complete documentation, see the included README.md and docs directory.*
