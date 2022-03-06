from IPython import get_ipython

from ._EndomillHaltException import EndomillHaltException
from .in_interactive_notebook import in_interactive_notebook


async def _ignore_code(*args, **kwargs):
    pass


def halt() -> None:
    if in_interactive_notebook():
        print('🌛💤 halting notebook via EndomillHaltException')
        raise EndomillHaltException
    else:
        print('🌛💤 disabling notebok by overriding IPython with nop runner')
        get_ipython().run_code = _ignore_code
        get_ipython().runcode = _ignore_code
