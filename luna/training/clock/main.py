"""Web server start module."""

import sys

from clock import create_app

def run(port=sys.argv[1] if len(sys.argv) > 1 else 5000):
    """Starts the web server."""
    create_app().run(port=port)

if __name__ == '__main__':
    run()
