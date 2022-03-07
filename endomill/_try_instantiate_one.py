import glob
from IPython.core.display import display, HTML
import itertools as it
from keyname import keyname as kn
from nbmetalog import nbmetalog as nbm
import papermill
from pathlib import Path
import shutil
from slugify import slugify
import tempfile
import typing

from .in_interactive_notebook import in_interactive_notebook


def _try_instantiate_one(parameter_pack: typing.Dict) -> None:

    before_notebook_paths = {*glob.glob('*.ipynb')}
    Path('executing.endomill.ipynb').touch()
    papermill.execute_notebook(
        nbm.get_notebook_path(),
        'executing.endomill.ipynb',
        parameters=parameter_pack,
        progress_bar=in_interactive_notebook(),
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        shutil.move('executing.endomill.ipynb', temp_dir)

        after_notebook_paths = {*glob.glob('*.ipynb')}
        new_notebook_paths \
            = after_notebook_paths - before_notebook_paths

        if not new_notebook_paths:
            new_notebook_path = kn.pack({
                **{
                    slugify(str(k)): slugify(str(v))
                    for k, v in parameter_pack.items()
                },
                **{
                    'ext': '.endomill.ipynb',
                },
            })
            try:
                shutil.copy(
                    f'{temp_dir}/executing.endomill.ipynb',
                    new_notebook_path,
                )
            except OSError:
                # filename too long
                for i in it.count():
                    fallback = f'fallback{i}.endomill.ipynb'
                    if not Path(fallback).exists():
                        new_notebook_path = fallback
                        shutil.copy(
                            f'{temp_dir}/executing.endomill.ipynb',
                            fallback,
                        )
                        break

            new_notebook_paths = {new_notebook_path}

        assert new_notebook_paths
        for new_notebook_path in new_notebook_paths:
            print('🪵✨ milled', new_notebook_path)
            display(HTML(
                '&nbsp;' * 8
                + f'📎 <a href="{new_notebook_path}">{new_notebook_path}</a>'
            ))
            print()
