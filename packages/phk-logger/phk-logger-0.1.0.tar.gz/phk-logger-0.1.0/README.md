# PHK-Logger

An uncomplicated way to use logger inside python applications

## Install
The easy way is by using pip
```bash
pip install phk-logger
```
  
The harder way is from sources
```bash
git clone https://github.com/proh4cktive/phk-logger.git
cd phk-logger
python install setup.py
```

## Usage
PHK-Logger is a lib so you just have to import it when needed
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from phk-logger import PHKLogger as Logger
```
  
Then in your code you can instantiate it directly
```python
logger = new Logger(name='mytest')
logger.infos('This is an info message')
```

## Options
PHK-Logger is configred by default to output log event to your SysLog sub-system (Only supports Linux/MacOS). Some additional options can be set in order to change this behaviour.  
- **name** Set a specific name to your logger stream, by default will use the `__name__` var.
- **level** Set the log level, must be a level from logging package
- **filename** If set phk-logger will output events to a specific filename using *TimedRotatingFileHandler* configured with a file rotating every midnight, and 3 backup files
- **backup** Only used if **filename** is configured, specifiy the number of backup to keep
- **when** Only used if **filename** is configured, specify when to execute the file rotation
- **cli** If set to True this will also output log event to command line interface (CLI). Only useful for debugging app.
- **pattern** Define the log pattern to use for event output. Default is `%(name)s %(asctime)s %(levelname)-8s %(message)s`



## Methods
Several methods can be used to generate event logs, they all support the same options only usefuls when using **cli** flag:  

- msg: the message to output
- color: override the default color
- light: override the light mode

> - **debug**(msg, color='blue', light=True) output event with prefix: `[*]`
> - **info**(msg, color='green', light=False) output event with prefix: `[+]`
> - **warning**(msg, color='yellow', light=False) output event with prefix: `[-]`
> - **error**(msg, color='red', light=False) output event with prefix: `[!]`
> - **critical**(msg, color='red', light=True) output event with prefix: `[!]`
  
An additional method is accessible which support a level parameter
> - **write**(message, level=None, color=None, light=None)

### Colors
Several colors are supported (case insensitive)
- BLACK
- BLUE
- GREEN
- CYAN
- RED
- PURPLE
- YELLOW
- WHITE
- no-color (default)

### Levels
Multiple levels are supported (case insensitive)
- DEBUG
- INFO
- INFOS
- WARNING
- ERROR
- CRITICAL
  

## TODO
- Unit Tests
- Doc