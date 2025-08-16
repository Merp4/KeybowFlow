# KeybowFlow GitHub Actions Workflows

This directory contains automated workflows for building and releasing KeybowFlow project artifacts.

## Workflows

### build-release.yml
**Purpose**: Builds complete release artifacts when a version tag is pushed

**Triggers**:
- Push of version tags (e.g., `v1.0.0`)
- Manual workflow dispatch

**Artifacts Created**:
- `keybowflow-device-files.zip` - Complete project ready for device
- `keybowflow-examples.zip` - Example configurations
- `circuitpython-keybow2040-9.2.8.uf2` - CircuitPython firmware
- `INSTALLATION.md` - Setup instructions
- `VERSION.txt` - Build information

**Usage**:
```bash
# Create and push a release tag
git tag v1.0.0
git push origin v1.0.0

# Or run manually from GitHub Actions tab
```

### test-build.yml  
**Purpose**: Validates project structure and build process on PRs and pushes

**Triggers**:
- Pull requests to main branch
- Pushes to main branch
- Manual workflow dispatch

**Validations**:
- Source file syntax checking
- Library download testing
- Package structure validation
- Example configuration checking

### Scripts

The workflows use a minimal script:
- `generate_release.py` - Generates release notes from template

All other build logic is embedded directly in the workflow YAML files for simplicity and transparency.

## Release Process

1. **Development**: Work on feature branches, test with `test-build.yml`
2. **Integration**: Merge to main branch 
3. **Release**: Create version tag to trigger `build-release.yml`
4. **Distribution**: Download artifacts from GitHub Releases

## For End Users

End users don't need to understand these workflows. They simply:
1. Go to GitHub Releases
2. Download `keybowflow-device-files.zip`
3. Extract to their Keybow 2040 device
4. Customize `keymap.py`

The workflows handle all the complexity of library management and packaging.
