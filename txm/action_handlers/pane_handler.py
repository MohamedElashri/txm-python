from ..tmux_wrapper import run_tmux_command

def split_pane_vertically():
    return run_tmux_command("tmux split-window")

def split_pane_horizontally():
    return run_tmux_command("tmux split-window -h")

def navigate_panes(direction):
    return run_tmux_command(f"tmux select-pane -{direction}")
