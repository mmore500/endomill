import _thread

from endomill._SigHandlerContextManager import SigHandlerContextManager


def test_SigHandlerContextManager():
    with SigHandlerContextManager() as h:
        _thread.interrupt_main()
        assert h.interrupted
