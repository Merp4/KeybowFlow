#!/usr/bin/env python3
"""
Generate release body from template for GitHub releases.
"""

import sys
import os
from pathlib import Path

def get_changelog_for_version(version):
    """Extract changelog for specific version from CHANGELOG.md."""
    changelog_path = Path(__file__).parent.parent.parent / "CHANGELOG.md"
    
    if not changelog_path.exists():
        return "See commit history for details"
    
    try:
        with open(changelog_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # For unreleased or if version not found, get [Unreleased] section
        if version.startswith('v'):
            version_check = version[1:]  # Remove 'v' prefix
        else:
            version_check = version
            
        # Extract [Unreleased] section (everything after [Unreleased] until next ##)
        lines = content.split('\n')
        changelog_lines = []
        in_unreleased = False
        
        for line in lines:
            if line.startswith('## [Unreleased]'):
                in_unreleased = True
                continue
            elif line.startswith('## [') and in_unreleased:
                break
            elif in_unreleased and line.strip():
                changelog_lines.append(line)
        
        if changelog_lines:
            return '\n'.join(changelog_lines).strip()
        else:
            return "See commit history for details"
    
    except Exception:
        return "See commit history for details"

def generate_release_body(version, firmware_version, commit_sha, changelog=None):
    """Generate release body from template."""
    
    # Get changelog from CHANGELOG.md if not provided
    if not changelog or changelog == "See commit history for details":
        changelog = get_changelog_for_version(version)
    
    # Read the template
    template_path = Path(__file__).parent / "RELEASE_TEMPLATE.md"
    
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    except FileNotFoundError:
        # Fallback template if file doesn't exist
        template = """# KeybowFlow Release {version}

### Quick Installation
1. Download `keybowflow-device-files.zip`
2. Extract to your Keybow 2040 CIRCUITPY drive
3. Edit `keymap.py` to customize

### Files Included
- keybowflow-device-files.zip (device-ready bundle)
- keybowflow-examples.zip (example configurations)
- circuitpython-keybow2040-{firmware_version}.uf2 (CircuitPython firmware)
- INSTALLATION.md (setup instructions)

### What's Changed
{changelog}

Built from commit: {commit_sha}"""

    # Replace placeholders
    release_body = template.format(
        version=version,
        firmware_version=firmware_version,
        commit_sha=commit_sha,
        changelog=changelog
    )
    
    return release_body

def main():
    """Main function."""
    if len(sys.argv) < 4:
        print("Usage: generate_release.py <version> <firmware_version> <commit_sha> [changelog]")
        print("Example: generate_release.py v1.0.0 9.2.8 abc123 'Added new features'")
        sys.exit(1)
    
    version = sys.argv[1]
    firmware_version = sys.argv[2]
    commit_sha = sys.argv[3]
    changelog = sys.argv[4] if len(sys.argv) > 4 else "See commit history for details"
    
    release_body = generate_release_body(version, firmware_version, commit_sha, changelog)
    print(release_body)

if __name__ == "__main__":
    main()
