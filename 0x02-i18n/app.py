#!/usr/bin/env python3
"""Mock logging in"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, get_locale
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime


class Config:
    """App configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """Return a user dictionary if ID is found, else None"""
    try:
        user_id = int(request.args.get("login_as"))
        return (users.get(user_id))
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set the current user if found"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Select the best language match based on priority:
    URL > user settings > request headers > default
    """
    # Locale from URL parameters
    locale_param = request.args.get('locale')
    if locale_param and locale_param in app.config['LANGUAGES']:
        return locale_param

    # Locale from user settings
    if g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    # Locale from request headers
    header_locale = request.accept_languages.best_match(
            app.config['LANGUAGES']
            )
    if header_locale:
        return header_locale

    # Default locale (Flask-Babel uses this if nothing is returned)
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """
    Select the best time zone based on:
    URL > user setting > default(UTC)
    """
    # Time zone from URL
    tz_param = request.args.get('timezone')
    if tz_param:
        try:
            return pytz.timezone(tz_param).zone
        except UnknownTimeZoneError:
            pass

    # Time zone from user settings
    if g.get('user'):
        user_tz = g.user.get('timezone')
        if user_tz:
            try:
                return pytz.timezone(user_tz).zone
            except UnknownTimeZoneError:
                pass
    # Default to UTC
    return 'UTC'


@app.route('/')
def index():
    """Render the main page with localized current time"""
    current_time = format_datetime(datetime.now())
    return (render_template(
            'index.html', locale=get_locale(),
            current_time=current_tim
            ))


if __name__ == "__main__":
    app.run()
