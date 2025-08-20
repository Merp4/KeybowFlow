#!/usr/bin/env python3
"""
Deployment script for copying runtime files to a CIRCUITPY device.
For manual use: copy src/*.py to your CIRCUITPY drive.
"""

import sys
import shutil
from pathlib import Path

def find_circuitpy():
    """Find CIRCUITPY drive on Windows."""
    for drive in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        boot_file = Path(f"{drive}:/boot_out.txt")
        if boot_file.exists():
            return Path(f"{drive}:")
    return None

def main():
    config = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # Find device
    device = find_circuitpy()
    if not device:
        print("CIRCUITPY device not found")
        print("Manual: copy src\\*.py to your device drive")
        sys.exit(1)
    
    print(f"Found device: {device}")
    
    # Copy config if specified
    if config:
        config_path = Path("examples/configs") / config
        if config_path.exists():
            shutil.copy2(config_path, "src/keymap.py")
            print(f"Using config: {config}")
    
    # Copy source files
    src_dir = Path("src")
    for py_file in src_dir.glob("*.py"):
        shutil.copy2(py_file, device / py_file.name)
        print(f"Copied: {py_file.name}")
    
    print("Deploy completed")

if __name__ == "__main__":
    main()
