from nbmetalog import nbmetalog as nbm
from os import path
import papermill
import shutil
import typing

from ._halt import halt
from ._try_instantiate_one import _try_instantiate_one


def instantiate_one(
    parameter_pack: typing.Dict,
    worker_id: int = 0,
    should_halt: bool = True,
) -> None:
    if path.exists(f'executing{worker_id}.endomill.ipynb'):
        print('detected executing.endomill.ipynb')
        print('skipping instantiate_one')
        return
    elif nbm.get_notebook_path().endswith('.endomill.ipynb'):
        print('detected .endomill.ipynb file extension')
        print('skipping instantiate_one')
        return

    try:
        print('👷🪓 milling', parameter_pack, '...')
        _try_instantiate_one(parameter_pack, worker_id)
    except papermill.PapermillExecutionError as e:
        print('papermill execution failed for parameters', parameter_pack)
        print('moving failed notebook to failed.endomill.ipynb')
        shutil.move(
            f'executing{worker_id}.endomill.ipynb', 'failed.endomill.ipynb'
        )
        raise e

    if should_halt:
        halt()
