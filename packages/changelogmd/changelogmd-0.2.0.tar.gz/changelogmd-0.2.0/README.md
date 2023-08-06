# py-changelogmd

Python module and CLI tool for CHANGELOG.md manipulation.

## Install

```
python3 -m pip install changelogmd
```

## Usage

```python3
from changelogmd import Changelog
changelog = Changelog("CHANGELOG.md")

# List available versions
print(list(changelog.versions))

# Print full Markdown
print(str(changelog))

# Print full Markdown of latest version
print(str(changelog.versions[0]))

# Bump release version from UNRELEASED version
changelog.bump()
```

### UNRELEASED changes

Unreleased changes are stored in the CHANGELOG.md file as top-most version

```markdown
# Changelog

## [UNRELEASED]

### Added
- New Feature added

### Removed
- This will cause a minor version bump
```
