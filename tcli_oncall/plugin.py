import click

ROLES = (
    'primary',
    'backup',
)

@click.group()
@click.version_option()
def oncall():
    """Manage on-call by explicitly taking roles.

    A plugin for teams that manage on-call handovers by requiring an explicit
    action by the next one on schedule.

    """
    pass


@oncall.command()
def roles():
    """List currenly configured on-call roles."""
    pass


@oncall.command()
@click.argument('role', type=click.Choice(ROLES))
def take():
    """Go on-call for the specified role."""
    pass


@oncall.command()
def show():
    """Show who is currently on-call."""
    pass


@oncall.command()
def schedule():
    """Open a link to the schedule."""
    pass


@oncall.command()
@click.option('--user', metavar='USER', help='Limit to a single user')
@click.option('--role', type=click.Choice(ROLES), help='Limit to a single role.')
def history(role):
    """List recent on-call history."""
    click.echo(role)


