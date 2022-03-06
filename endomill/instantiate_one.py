from nbmetalog import nbmetalog as nbm
from os import path
import papermill
import shutil
import typing

from ._halt import halt
from ._try_instantiate_one import _try_instantiate_one


def instantiate_one(
    parameter_pack: typing.Dict,
    should_halt: bool = True,
) -> None:
    if path.exists('executing.endomill.ipynb'):
        print('detected executing.endomill.ipynb')
        print('skipping instantiate_one')
        return
    elif nbm.get_notebook_path().endswith('.endomill.ipynb'):
        print('detected .endomill.ipynb file extension')
        print('skipping instantiate_one')
        return

    try:
        print('👷🪓 milling', parameter_pack, '...')
        _try_instantiate_one(parameter_pack)
    except papermill.PapermillExecutionError as e:
        print('papermill execution failed for parameters', parameter_pack)
        print('moving failed notebook to failed.endomill.ipynb')
        shutil.move('executing.endomill.ipynb', 'failed.endomill.ipynb')
        raise e

    if should_halt:
        halt()
