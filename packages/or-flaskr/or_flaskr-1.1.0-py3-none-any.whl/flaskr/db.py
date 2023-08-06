# Connect to the Database
# The first thing to do when working with a SQLite database
# (and most other Python database libraries) is to create a connection to it.
# Any queries and operations are performed using the connection,
# which is closed after the work is finished.

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


# Add the Python functions that will run these SQL commands to the db.py file

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# The close_db and init_db_command functions need to be registered with the application instance;
# otherwise, they won’t be used by the application.
# write a function that takes an application and does the registration.    

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)