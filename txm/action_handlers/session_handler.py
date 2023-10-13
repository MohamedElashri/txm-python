from ..tmux_wrapper import run_tmux_command
def create_session(session_name):
    return run_tmux_command(f"tmux new-session -d -s {session_name}")

def list_sessions():
    return run_tmux_command("tmux list-sessions")

def attach_session(session_name):
    return run_tmux_command(f"tmux attach-session -t {session_name}")

def detach_session():
    return run_tmux_command("tmux detach-client")
