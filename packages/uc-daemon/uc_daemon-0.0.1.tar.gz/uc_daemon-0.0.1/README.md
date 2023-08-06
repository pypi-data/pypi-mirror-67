# uc_daemon  
A set of classes and functions for demonizing a process and related tools.  

It is part of the Unicon project.

https://unicon.10k.me

## Usage:

##### Install
```sh
pip install --user uc-daemon
```
##### and use

```python
import uc_daemon
```

## Functions:

**daemonize()**

Become a daemon.
To base process returns daemonized process id on successful and less than zero on fails.
To daemonized process returns zero.

**redirectio(handle)**

Redirects standart descriptors to specified file handle.

## Global constants

**LOGGER**

You may override this constant to manage debugging messages.

## Example:

```python
import os
import sys
import uc_daemon

pid = uc_daemon.daemonize()

if (pid == 0):
    print("I'm daemon! My pid is %d" % os.getpid())
else:
    print("Daemon started with pid %d and my pid is %d" % (pid, os.getpid()))    
```
