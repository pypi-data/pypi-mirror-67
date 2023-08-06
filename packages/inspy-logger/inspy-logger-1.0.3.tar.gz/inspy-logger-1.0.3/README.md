# InSPy Logger

## Description

InSPy Logger is a library package made for Python3, and is installable in any environment that has 
access to PIP for Python3 and an internet connection.

***InSPy Logger** *could work on Python2, but it hasn't been tested as of this writing*

## Notice

Please read STATEMENT.md in the docs/ directory for some important information that you might want if you're planning
 on using InSPy Logger as a dependency in any application/library that you plan on maintaining

## Usage

```python

import inspy_logger as logger

app_name = str("MyApplication")

log = logger.start(app_name, debug=True)
log.info('This is a log entry of level: INFO')
log.warning('This is a log entry of level: WARNING')
log.debug('This is a log entry of level: DEBUG')

```

The above code would produce the following log entries in the relative terminal:

![](examples/images/inspy_logger_readme_screenie_1.png)
