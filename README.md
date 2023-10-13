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
  - [Contributing](#contributing)
  - [License](#license)

## Installation

To install `txm`, navigate to the root directory of the project and execute the following command:

```bash
cd txm
pip install -e .
```

This will install the package in editable mode, making it accessible from the command line.

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

`txm` can optionally read from a `.txm-config.json` file located in the root directory for user-specific settings. This feature is a placeholder for future implementations.

## Contributing

Contributions are welcome. Please read the CONTRIBUTING.md for guidelines.

## License

This project is licensed under the MIT License. See the LICENSE.md file for details.
