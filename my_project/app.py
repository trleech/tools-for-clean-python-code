"""app"""

from flask import Flask, jsonify


def create_app():
    """
    Creates a flask app
    """
    app = Flask("my_project")

    @app.route("/", methods=["GET"])
    def index():
        """Handler for website index"""
        return jsonify({"Hello": "world"})

    return app
