import sqlite3

import click
from flask import current_app, g


def get_db() -> sqlite3.Connection:
    """Returns the connection to the database

    Returns:
        g.db(sqlite3.Connection): the database connection
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(_e=None) -> None:
    """Closes the database connection

    Args:
        _e(Any): Optional parameter to capture an exception
    """
    db: sqlite3.Connection = g.pop('db', None)

    if db is not None:
        db.close()


def init_db() -> None:
    """Initializes the database by executing schema.sql file"""
    db: sqlite3.Connection = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command() -> None:
    """Implements a CLI command for executing init_db function"""
    init_db()
    click.echo('Initialized the database.')


def init_app(app) -> None:
    """Registers teardown and CLI functions in the Flask application"""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
