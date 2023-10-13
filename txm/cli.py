import click
from action_handlers.session_handler import create_session, list_sessions, attach_session, detach_session
from action_handlers.pane_handler import split_pane_vertically, split_pane_horizontally, navigate_panes
from action_handlers.command_handler import execute_command
from config_manager import load_config

@click.group()
def txm():
    config = load_config()
    # Further initializations can go here

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

if __name__ == "__main__":
    txm()
