import sys
from os import environ
from subprocess import Popen


def main():
    if len(sys.argv) == 1:
        from .orsj import app
        from .orsj.views import setting  # noqa

        HOST = environ.get("SERVER_HOST", "0.0.0.0")
        try:
            PORT = int(environ.get("SERVER_PORT", "5000"))
        except ValueError:
            PORT = 5000
        app.config["MAX_CONTENT_LENGTH"] = int(
            environ.get("MAX_CONTENT_LENGTH", "2100200")
        )
        # app.debug = True
        app.run(HOST, PORT)
    else:
        p = Popen(["redis-server"])
        p.wait()
