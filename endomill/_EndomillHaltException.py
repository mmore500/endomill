from io import StringIO
import sys


# adapted from https://stackoverflow.com/a/48000614/17332200
class EndomillHaltException(SystemExit):
    """Exception temporarily redirects stderr to buffer."""

    def __init__(self):
        sys.stderr = StringIO()

    def __del__(self):
        sys.stderr.close()
        sys.stderr = sys.__stderr__  # restore from backup
