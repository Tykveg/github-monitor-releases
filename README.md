# Github Monitor Releases

This small python script monitors github repositories releases (tags) so you will be notified of an update without having to open the repository page (if it doesn't have auto-updates). But you still have to update binaries/files manually.\
\
I made this small script for myself because some repositories don't have auto updates so I don't have to monitor them manually. But I don't mind publishing this script. Maybe someone will find it useful.

## Installation

Download the source code from the [releases page](https://github.com/Tykveg/github-monitor-releases/releases) and extract it from the zip archive.\
You can use [virtual environment](https://docs.python.org/3/library/venv.html).\
You also need to install [requests](https://pypi.org/project/requests/) library:
```bash
pip install requests
```
And that's it.

## Usage

In the script's folder add the file `repos.txt` and add repositories links with their version tags. See `repo-example.txt`:
```
# This is a comment
# And you can have empty lines

# Format:
# https://github.com/NAME/REPO VERSION_TAG
https://github.com/psf/requests v2.30.0 # Also a comment. You can put one or less spaces between '#' and the version tag name.
# You can have a repository url without the version, but the script will warn you about it.
https://github.com/psf/requests # <- will show error but won't crash

```
And then just run `github-monitor-releases`. Outdated repositories will have a `[NEW]` tag. After the update you have to manually change the version tag in `repos.txt` so that the script stops notifying you.

## Contributing

Refactoring and TYPO fixes are welcome. Feel free to suggest new features as well. Thank you!

## Licence

[MIT](https://github.com/Tykveg/github-monitor-releases/blob/main/LICENSE)

