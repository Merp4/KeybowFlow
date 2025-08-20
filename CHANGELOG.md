# KeybowFlow Changelog

## [Unreleased]

### Added

- Hardware testing validation on actual Keybow 2040 device
- Comprehensive key reference documentation (KEY_REFERENCE.md, ACTION_REFERENCE.md)
- Logical key position mapping system (R0=top, R3=bottom)
- 7 example configurations with practical multi-layer setups

### Changed

- Simplified version management (single source of truth in workflows)
- Consolidated configuration system in constants.py
- Adjusted documentation tone to be neutral
- Fixed requirements.txt version consistency with bundle approach

### Removed

- Legacy backward compatibility code
- Complex sync scripts (favor simple file copying)
- Excessive promotional language from documentation
- Wide version ranges that conflicted with bundle pinning

## [1.0.0] - Initial Release

### Features

- Initial Keybow 2040 CircuitPython project
- Basic configuration system
- PMK library integration
- Adafruit HID library support
- Example configurations
- GitHub Actions build pipeline
