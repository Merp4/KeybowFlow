# Version management

Keep tooling pins (for example `circup`) in `requirements.txt`. To update a tool version, edit `requirements.txt` and commit; CI installs from that file. Avoid duplicating the same pin elsewhere (for example in workflow `env` entries).

## Version sources

- **CircuitPython Bundle**: [Adafruit CircuitPython Bundle releases](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases)
- **CircUp**: [circup on PyPI](https://pypi.org/project/circup/)
