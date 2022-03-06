from nbmetalog import nbmetalog as nbm
from os import path
import typing

from ._halt import halt
from .instantiate_one import instantiate_one


def instantiate_over(
    parameter_packs: typing.Iterable[typing.Dict],
    should_halt: bool = True,
) -> None:
    if path.exists('executing.endomill.ipynb'):
        print('detected executing.endomill.ipynb file')
        print('skipping instantiate_over')
        return
    elif nbm.get_notebook_path().endswith('.endomill.ipynb'):
        print('detected .endomill.ipynb file extension')
        print('skipping instantiate_one')
        return

    for parameter_pack in parameter_packs:
        instantiate_one(parameter_pack, should_halt=False)

    print('🏠🍻 milling complete!')

    if should_halt:
        halt()
