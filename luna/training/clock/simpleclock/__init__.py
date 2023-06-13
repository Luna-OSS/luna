import flask

def create_app():
    """Returns the Flask app."""

    app = flask.Flask(__name__)

    @app.route('/')
    def index():
        """Display the current time."""
        return flask.render_template('index.html')

    return app
