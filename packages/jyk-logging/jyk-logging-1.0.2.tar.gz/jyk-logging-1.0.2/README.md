# jyk-logging

jyk logging utils


## Installation
```
$ pip install jyk-logging
```

## Getting Started

1. Cases

```shell
import logging
from jyk.logging import initConsoleLogging, initLogging, LogRootPath, FormatterMode

# case 1: initConsoleLogging(level=logging.INFO, mode=FormatterMode.BRIEF)
initConsoleLogging()

# case 2: initLogging(name, level=logging.INFO, mode=FormatterMode.INTACT):
LogRootPath.set('var/log/jyk')
initLogging('test.log')
```

2. API

```python
def initConsoleLogging(level=logging.INFO, mode=FormatterMode.BRIEF):
    """Initializes logging only to console.
    Args:
        level: logging.level
    """

def initLogging(name, level=logging.INFO, mode=FormatterMode.INTACT):
    """Initializes logging.
    Args:
        level: logging.level
    """

class FormatterMode(object):
    BRIEF = "brief"
    INTACT = 'intact'

if mode == FormatterMode.INTACT:
    formatter = logging.Formatter(
        "%(asctime)s [%(name)s] %(levelname)s: %(message)s")
else:
    formatter = logging.Formatter("[%(name)s]: %(message)s")

```


## Running the tests

```shell
$ cd jyk-logging
$ pytest -s
```

## Changelog

## 1.0.2
> 2020-04-22 release

### BugFix

- fix encoding

## 1.0.1
> 2019-10-19 release

### Features

- add initConsoleLogging
- add initLogging
- add LogRootPath
- add FormatterMode

## TODOs

- add color api

## Authors

* **kongkong Jiang** - *Initial work* - [jyker](https://git.kongkongss.com/jyker)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
