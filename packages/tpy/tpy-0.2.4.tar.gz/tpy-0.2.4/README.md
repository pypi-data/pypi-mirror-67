# tpy

## Installation

```bash
pip install tpy
```


## Usage

See `tpy --help`:

```
usage: tpy [--session SESSION] [--window WINDOW] [--reset-window]
           [--reset-pane] [--dry] [-h]
           {cmd,again} ...

Runs commands in tmux.

positional arguments:
  {cmd,again}

optional arguments:
  --session SESSION  Name of session to use
  --window WINDOW    Name of window to use
  --reset-window     Resets window before execution
  --reset-pane       Resets pane before execution
  --dry              Will send but not execute commands
  -h, --help         Usage info


usage: tpy cmd command

Runs arbitrary command.

positional arguments:
  command  Command to execute



usage: tpy again [-tu TIMES_UP]

Runs previous command again.

optional arguments:
  -tu TIMES_UP, --times-up TIMES_UP
                        Number of times to press cursor up
```
