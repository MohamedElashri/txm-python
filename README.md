
# All Development and update is now done in [txm](https://github.com/MohamedElashri/txm) new repository and now using Go as a development language. This is now archived

# txm - A Tmux Helper Tool

`txm` is a command-line utility to make working with [tmux](https://github.com/tmux/tmux/wiki) more efficient and user-friendly. It's written in Python and aims to abstract some of the complexities involved in managing tmux sessions, panes, and command executions.

## Table of Contents

- [txm - A Tmux Helper Tool](#txm---a-tmux-helper-tool)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Session Management](#session-management)
      - [Create a New Session](#create-a-new-session)
      - [List All Sessions](#list-all-sessions)
      - [Attach to a Session](#attach-to-a-session)
      - [Detach from a Session](#detach-from-a-session)
    - [Pane Management](#pane-management)
      - [Split Pane Vertically](#split-pane-vertically)
      - [Split Pane Horizontally](#split-pane-horizontally)
      - [Navigate Between Panes](#navigate-between-panes)
    - [Command Execution](#command-execution)
      - [Execute a Command](#execute-a-command)
  - [Configuration](#configuration)
    - [.txm-config.json](#txm-configjson)
    - [.txm-presets.json](#txm-presetsjson)
  - [Contributing](#contributing)
  - [License](#license)
## Installation

You can install the package from PyPI using `pip`:

```bash
pip install txm
```



To build `txm` from the source first clone the repository

```bash
git clone https://github.com/MohamedElashri/txm
```

Now navigate to the root directory of the project and execute the following command:

```bash
cd txm
pip install .
```

## Usage

Here are the available functionalities of `txm`.

### Session Management

#### Create a New Session

To create a new session, run:

```bash
txm new [SESSION_NAME]
```

#### List All Sessions

To list all available sessions, run:

```bash
txm list
```

#### Attach to a Session

To attach to an existing session, run:

```bash
txm attach [SESSION_NAME]
```

#### Detach from a Session

To detach from the current session, run:

```bash
txm detach
```

### Pane Management

#### Split Pane Vertically

To split the current pane vertically, run:

```bash
txm vsplit
```

#### Split Pane Horizontally

To split the current pane horizontally, run:

```bash
txm hsplit
```

#### Navigate Between Panes

To navigate between panes, run:

```bash
txm navigate [DIRECTION]
```
`DIRECTION` can be one of the following: `U` for up, `D` for down, `L` for left, `R` for right.

### Command Execution

#### Execute a Command

To execute a command in the current pane, run:

```bash
txm run [COMMAND]
```

## Configuration

`txm` can optionally read from a `.txm-config.json` file located in the root directory for user-specific settings. 

### .txm-config.json
This configuration file contains settings and preferences for your TXM utility. It should be placed in the root directory of your project or your home directory.

**Default Template:** 

```json 
{
  "tmux_path": "/usr/local/bin/tmux",
  "log_directory": "logs/",
  "default_session_name": "my_session"
}
```

- **tmux_path**: Specifies the path to the tmux executable.
- **log_directory**: Specifies the directory where tmux pane logs will be saved.
- **default_session_name**: Specifies the default name for a new tmux session.


### .txm-presets.json
This file holds the saved tmux session presets. It will be automatically generated by the `txm save` command, or you can create it manually in the directory of your choice.

**Default Template:**

```json
{
  "presets": [
    {
      "name": "preset_1",
      "windows": [
        {
          "name": "window_1",
          "panes": ["command1", "command2"]
        },
        {
          "name": "window_2",
          "panes": ["command3", "command4"]
        }
      ]
    }
  ]
}
```

- **name**: Specifies the name of the saved preset.
- **windows**: Array of windows in the preset.
  - **name**: Name of the window.
  - **panes**: Array of commands to run in each pane.
## Contributing

Contributions are welcome. Feel free to open a pull request or submit an issue.

## License

This project is licensed under the MIT License. See the LICENSE.md file for details.
