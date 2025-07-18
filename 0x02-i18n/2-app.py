#!/usr/bin/env python3
"""Flask app with basic Babel setup"""


from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """App configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match with supported languages"""
    return (request.accept_languages.best_match(app.config['LANGUAGES']))


@app.route('/')
def index():
    """Render the index page"""
    return (render_template('2-index.html'))


if __name__ == '__main__':
    app.run()
