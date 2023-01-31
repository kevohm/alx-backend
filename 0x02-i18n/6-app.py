#!/usr/bin/env python3
"""0-app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """ Config file class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get the current locale
    """
    URL_locale = request.args.get("locale")
    data = app.config["LANGUAGES"]
    user = g.user
    if URL_locale is not None and URL_locale in data:
        return URL_locale
    elif user is not None:
        locale = user["locale"]
        if locale is not None and locale in data:
            return locale
    elif request.accept_languages is not None:
        return request.accept_languages.best_match(data)
    else:
        return app.config["BABEL_DEFAULT_LOCALE"]


@app.before_request
def before_request():
    """set user globally
    """
    g.user = get_user()


def get_user():
    """ get logged in User
    """
    users = {
            1: {"name": "Balou", "locale": "fr",
                "timezone": "Europe/Paris"},
            2: {"name": "Beyonce", "locale": "en",
                "timezone": "US/Central"},
            3: {"name": "Spock", "locale": "kg",
                "timezone": "Vulcan"},
            4: {"name": "Teletubby", "locale": None,
                "timezone": "Europe/London"},
            }
    index = request.args.get('login_as')
    if index is not None:
        index = int(index)
        if index in users.keys():
            return users[index]
    return None


@app.route("/")
def hello_world():
    return render_template("6-index.html", user=g.user)


if __name__ == "__main__":
    app.run()
