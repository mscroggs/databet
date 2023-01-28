"""Script to increase the version number."""

import json
from datetime import datetime

# Calculate new version number
with open("VERSION") as f:
    version = tuple(int(i) for i in f.read().split("."))

now = datetime.now()
if now.year == version[0] and now.month == version[1]:
    new_version = (now.year, now.month, version[2] + 1)
else:
    new_version = (now.year, now.month, 1)
new_version_str = ".".join([f"{i}" for i in new_version])

# VERSION file
with open("VERSION", "w") as f:
    f.write(new_version_str)

# setup.py
new_setup = ""
with open("setup.py") as f:
    for line in f:
        if 'version="' in line:
            a, b = line.split('version="')
            b = b.split('"', 1)[1]
            new_setup += f'{a}version="{new_version_str}"{b}'
        else:
            new_setup += line
with open("setup.py", "w") as f:
    f.write(new_setup)

# databet/version.py
with open("databet/version.py", "w") as f:
    f.write(f'"""Version number."""\n\nversion = "{new_version_str}"\n')

print(f"Updated version to {new_version_str}")
