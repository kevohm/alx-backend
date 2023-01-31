#!/usr/bin/env python3
"""0-app
"""
from flask import Flask, render_template, request
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
    locale = request.args.get('locale')
    data = app.config["LANGUAGES"]
    if locale is not None:
        if locale in data:
            return locale
    return request.accept_languages.best_match(data)


@app.route("/")
def hello_world():
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
