from flask import Blueprint, render_template

from flask_db_app.db import get_db

bp = Blueprint('flask_db_app', __name__)


@bp.route('/names/')
def count_unique_artists() -> str:
    """Returns a template with the count of unique artists

    Returns:
        template(str): rendered HTML template
    """
    query = 'SELECT COUNT(DISTINCT artist) FROM tracks;'

    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        count = cursor.fetchone()[0]

    template = render_template('unique_artists.html',
                               count=count)
    return template


@bp.route('/tracks/')
def count_tracks() -> str:
    """Returns a template with the count of all tracks

    Returns:
        template(str): rendered HTML template
    """
    query = 'SELECT COUNT(id) FROM tracks;'

    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        count = cursor.fetchone()[0]

    template = render_template('count_tracks.html',
                               count=count)
    return template


@bp.route('/tracks/<genre>')
def count_genre_tracks(genre) -> str:
    """Returns a template with the count of all tracks of
    specified genre

    Args:
        genre(str): the genre of the track

    Returns:
        template(str): rendered HTML template
    """
    query = 'SELECT COUNT(id) FROM tracks WHERE genre = ?;'

    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (genre,))
        count = cursor.fetchone()[0]

    template = render_template('count_genre_tracks.html',
                               count=count)
    return template


@bp.route('/tracks-sec/')
def tracks_time() -> str:
    """Returns a template with all track names and their length

    Returns:
        template(str): rendered HTML template
    """
    query = 'SELECT title, length FROM tracks;'

    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        tracks = cursor.fetchall()

    template = render_template('tracks_time.html',
                               tracks=tracks)
    return template


@bp.route('/tracks-sec/statistics/')
def get_stats():
    """Returns a template with average track length and total
    length of all tracks

    Returns:
        template(str): rendered HTML template
    """
    query = 'SELECT AVG(length), SUM(length) FROM tracks;'

    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        average, total = cursor.fetchone()

    template = render_template('tracks_stats.html',
                               average=int(average),
                               total=total)
    return template
