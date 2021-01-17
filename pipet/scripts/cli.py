import click

@click.group()
def pipet():
    pass

@click.command()
def create():
    '''automatically create flask web app'''
    print("create!!")


@click.command()
@click.option(
    '-n',
    '--name',
    'name',
    default='name',
    show_default=True
)
@click.option(
    '--db',
    'database',
    type=click.Choice(('sqlite3','postgresql','mysql')),
    default='sqlite3',
)
def json(name,database):
    '''create_json_project'''
    print(name,database)
    print("json!!")


@click.command()
def status():
    '''print_current_project status'''
    print('No Project')

pipet.add_command(create)
pipet.add_command(json)
pipet.add_command(status)

if __name__=='__main__':
    pipet()
