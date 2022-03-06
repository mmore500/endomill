from IPython.display import display, Javascript
import time
import threading

from ._SigHandlerContextManager import SigHandlerContextManager


def in_interactive_notebook() -> bool:
    with SigHandlerContextManager() as h:
        thread = threading.Thread(
            target=lambda: display(Javascript(
                'Jupyter.notebook.kernel.interrupt()'
            )),
        )
        thread.start()
        thread.join()

        time.sleep(0.2)

        return h.interrupted

    # possible alternate implementation
    # import ipynbname
    # try:
    #     ipynbname.path()
    #     return True
    # except:
    #     return False
