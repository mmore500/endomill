import nbformat
from nbclient import NotebookClient
import os
from os.path import dirname, exists, realpath

from endomill._unlink_missing_ok import unlink_missing_ok


def test_instance_outpath():
    # pre cleanup
    worker_id = 0
    unlink_missing_ok(f'executing{worker_id}.endomill.ipynb')
    unlink_missing_ok('failed.endomill.ipynb')
    unlink_missing_ok('instance_outpath.endomill.ipynb')
    unlink_missing_ok('parameter=value+ext=.endomill.ipynb')

    notebook_path \
        = f'{dirname(realpath(__file__))}/assets/add_instance_outpath.ipynb'
    os.environ['NOTEBOOK_PATH'] = notebook_path
    nb = nbformat.read(
        notebook_path,
        as_version=4,
    )
    client = NotebookClient(nb)
    print("before executing")
    client.execute()
    print("executing")

    assert exists('instance_outpath.endomill.ipynb')
    assert not exists(f'executing{worker_id}.endomill.ipynb')
    assert not exists('failed.endomill.ipynb')
    assert not exists('parameter=value+ext=.endomill.ipynb')

    # post cleanup
    unlink_missing_ok('instance_outpath.endomill.ipynb')
