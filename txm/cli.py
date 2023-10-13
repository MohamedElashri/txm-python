import click
from .action_handlers.session_handler import create_session, list_sessions, attach_session, detach_session
from .action_handlers.pane_handler import split_pane_vertically, split_pane_horizontally, navigate_panes
from .action_handlers.command_handler import execute_command
from .config_manager import load_config
from .txm_core import PresetManager, LogManager, SyncManager

@click.group()
def txm():
    config = load_config()

@txm.command()
@click.argument("session_name")
def new(session_name):
    click.echo(create_session(session_name))

@txm.command()
def list():
    click.echo(list_sessions())

@txm.command()
@click.argument("session_name")
def attach(session_name):
    click.echo(attach_session(session_name))

@txm.command()
def detach():
    click.echo(detach_session())

@txm.command()
def vsplit():
    click.echo(split_pane_vertically())

@txm.command()
def hsplit():
    click.echo(split_pane_horizontally())

@txm.command()
@click.argument("direction")
def navigate(direction):
    click.echo(navigate_panes(direction))

@txm.command()
@click.argument("command")
def run(command):
    click.echo(execute_command(command))

# New features

@txm.command()
@click.argument("preset_name")
def save_preset(preset_name):
    click.echo(PresetManager.handle_save(preset_name))

@txm.command()
@click.argument("preset_name")
def load_preset(preset_name):
    click.echo(PresetManager.handle_load(preset_name))

@txm.command()
@click.argument("preset_name")
def remove_preset(preset_name):
    click.echo(PresetManager.handle_remove(preset_name))

@txm.command()
def list_presets():
    click.echo(PresetManager.handle_list())

@txm.command()
@click.argument("pane_id")
def start_log(pane_id):
    click.echo(LogManager.handle_start(pane_id))

@txm.command()
@click.argument("pane_id")
def stop_log(pane_id):
    click.echo(LogManager.handle_stop(pane_id))

@txm.command()
@click.argument("pane_id")
def show_log(pane_id):
    click.echo(LogManager.handle_show(pane_id))

@txm.command()
@click.argument("operation")
def sync_panes(operation):
    click.echo(SyncManager.handle_sync(operation))

if __name__ == "__main__":
    txm()
