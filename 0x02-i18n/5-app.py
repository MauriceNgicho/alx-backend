#!/usr/bin/env python3
"""Mock logging in"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, get_locale


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
    """Select best language match"""
    user_locale = request.args.get('locale')
    if user_locale and user_locale in app.config['LANGUAGES']:
        return (user_locale)
    return (request.accept_languages.best_match(app.config['LANGUAGES']))


@app.route('/')
def index():
    """Render the main page"""
    return (render_template('5-index.html', locale=str(get_locale())))


if __name__ == "__main__":
    app.run()
