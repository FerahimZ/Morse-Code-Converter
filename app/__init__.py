from flask import Flask


def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "\x03C\xccR\xa9y\x0f\xf1\x85\xa0\x00m"

    from app.views import morse
    app.register_blueprint(morse)

    return app





