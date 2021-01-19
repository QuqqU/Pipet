import click


@click.group()
@click.help_option('--help', '-h')
def pipet():
    pass


@click.command(help='automatically create flask web app')
def create():
    print("create!!")


@click.command(help='create_json_project')
@click.option(
    '-n', '--name',
    'name',
    default='new_project',
    show_default=True
)
@click.option(
    '--db',
    'database',
    type=click.Choice(('sqlite3', 'postgresql', 'mysql')),
    default='sqlite3',
    show_default=True
)
def create_json(name, database):
    print(name, database)
    print("json!!")


@click.command(help='print_current_project status')
def status():
    print('No Project')


pipet.add_command(create)
pipet.add_command(create_json)
pipet.add_command(status)

if __name__ == '__main__':
    pipet()
