#!/usr/bin/env python3
"""Flask app with basic Babel setup"""


from flask import Flask, render_template, request
from flask_babel import Babel, _, get_locale


class Config:
    """App configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)
# Avail get_locale to Jinja templates
app.jinja_env.globals['get_locale'] = get_locale


@babel.localeselector
def get_locale():
    """Determine the best match with supported languages"""
    preferred = request.accept_languages.best_match(app.config['LANGUAGES'])
    return (preferred)


@app.route('/')
def index():
    """Render the index page"""
    return (render_template('3-index.html'))


if __name__ == '__main__':
    app.run()
