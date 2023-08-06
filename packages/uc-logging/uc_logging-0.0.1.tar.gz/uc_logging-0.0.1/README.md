# uc_logging  
A set of classes and functions that extend the log package.  

It is part of the Unicon project.

https://unicon.10k.me

## Usage:

##### Install
```sh
pip install --user uc-logging
```
##### and use

```python
import uc_logging
```

## Functions:



## Classes:

**Formatter(default=logging.BASIC_FORMAT, formats=None)**

Multi formatter.
Adds the ability to format log messages based on their level.

Formats is a dict where key is a level and value it's a format.

**UnbufferedStreamHandler(stream)**

Unbuffered stream handler.

When multiprocessing queue is used (for example), standard output may stuck. Common flushing not working. Using -u option not guaranteed (it helps). So write directly.

## Example:

```python
import logging
import uc_logging

format_standard_a = "%(asctime)s [%(levelname)s] - %(message)s"
format_standard_d = "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s"

logger = logging.getLogger("formatter_test")
logger.handlers.clear()
logger.setLevel(logging.DEBUG)
# Set multi formatter
formatter = uc_logging.Formatter(default=format_standard_a, formats={logging.DEBUG: format_standard_d})
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("TEST FORMATTER.")
logger.debug("TEST FORMATTER.")
```
