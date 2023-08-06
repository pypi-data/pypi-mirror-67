# tpy

## Installation

```bash
pip install tpy
```


## Usage

See `tpy --help`:

```
usage: tpy [--session SESSION] [--window WINDOW] [--reset-window]
           [--reset-pane] [--dir DIR] [--dry] [-h]
           {cmd,again,pytest,python} ...

Runs commands in tmux.

positional arguments:
  {cmd,again,pytest,python}

optional arguments:
  --session SESSION     Session to use
  --window WINDOW       Window to use
  --reset-window        Resets window before execution
  --reset-pane          Resets pane before execution
  --dir DIR             Changes into directory for execution
  --dry                 Will send but not execute commands
  -h, --help            Usage info


usage: tpy cmd command

Runs arbitrary command.

positional arguments:
  command  Command to execute



usage: tpy again [-tu TIMES_UP]

Runs previous command again.

optional arguments:
  -tu TIMES_UP, --times-up TIMES_UP
                        Number of times to press cursor up



usage: tpy pytest [-e EXECUTABLE] [--ipdb] file_or_dir

Runs pytest on file or directory. Any additional arguments are passed on.

positional arguments:
  file_or_dir

optional arguments:
  -e EXECUTABLE, --executable EXECUTABLE
                        pytest executable
  --ipdb                Enables ipdb



usage: tpy python [-e EXECUTABLE] [--pdb] [--ipdb] file

Executes file with python. Any additional arguments are passed on.

positional arguments:
  file

optional arguments:
  -e EXECUTABLE, --executable EXECUTABLE
                        Python executable
  --pdb                 Enables pdb
  --ipdb                Enables ipdb
```
