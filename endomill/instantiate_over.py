# import asyncio
import functools
import glob
import itertools as it
import nest_asyncio
from os import path
import typing
import warnings

from nbmetalog import nbmetalog as nbm

from ._halt import halt
from ._NestablePool import NestablePool
from .instantiate_one import instantiate_one

def instantiate_over(
    parameter_packs: typing.Iterable[typing.Dict],
    max_workers: int = 1,
    should_halt: bool = True,
) -> None:
    if glob.glob('executing*.endomill.ipynb'):
        print('detected executing.endomill.ipynb file')
        print('skipping instantiate_over')
        return
    elif nbm.get_notebook_path().endswith('.endomill.ipynb'):
        print('detected .endomill.ipynb file extension')
        print('skipping instantiate_one')
        return
    try:
        # asyncio.set_event_loop(asyncio.new_event_loop())
        nest_asyncio.apply()
        with NestablePool(max_workers) as pool:
            pool.starmap(
                functools.partial(instantiate_one, should_halt=False),
                zip(parameter_packs, it.count()),
            )
    except RuntimeError:
        warnings.warn("multiprocesing failed, falling back to serial processing")
        for pp, idx in zip(parameter_packs, it.count()):
            instantiate_one(pp, idx, should_halt=False)

    print('🏠🍻 milling complete!')

    if should_halt:
        halt()
