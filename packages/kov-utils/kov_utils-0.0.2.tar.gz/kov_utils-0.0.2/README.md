# kov-utils ![Python 3.6](https://img.shields.io/static/v1?label=Python&message=3.6%20|%203.7&color=blue)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install kov-utils.

```bash
pip install kov-utils
```

## Modules

kjson.py - json save and load

paths.py - paths and file extensions

rand.py - generate random string and sleep mechanism

request.py - request with retry mechanism

sh.py - subprocess commands

strings.py - string utilities

## Example

```python
from kov_utils import strings

string_between('kov_utilstestingphase', 'kov_utils', 'phase') #string, from, to
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
