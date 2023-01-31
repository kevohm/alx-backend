#!/usr/bin/env python3
"""0-app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Config file class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "en"
    BABEL_DEFAULT_LOCALE = "fr"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get the current locale
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello_world():
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
