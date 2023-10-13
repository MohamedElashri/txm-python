from ..tmux_wrapper import run_tmux_command

def execute_command(command):
    return run_tmux_command(f"tmux send-keys \"{command}\" C-m")
