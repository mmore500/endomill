import nbformat
from nbclient import NotebookClient
import os
from os.path import dirname, exists, realpath

from endomill._unlink_missing_ok import unlink_missing_ok


def test_intantiate_one():
    # pre cleanup
    unlink_missing_ok('parameter=value+ext=.endomill.ipynb')
    unlink_missing_ok('executing.endomill.ipynb')
    unlink_missing_ok('failed.endomill.ipynb')

    notebook_path \
        = f'{dirname(realpath(__file__))}/assets/instantiate_one.ipynb'
    os.environ['NOTEBOOK_PATH'] = notebook_path
    nb = nbformat.read(
        notebook_path,
        as_version=4,
    )
    client = NotebookClient(nb)
    client.execute()

    assert not exists('failed.endomill.ipynb')
    assert not exists('executing.endomill.ipynb')
    assert exists('parameter=value+ext=.endomill.ipynb')

    # post cleanup
    unlink_missing_ok('parameter=value+ext=.endomill.ipynb')


def test_intantiate_url():
    # pre cleanup
    unlink_missing_ok('parameter=https-example-com+ext=.endomill.ipynb')
    unlink_missing_ok('executing.endomill.ipynb')
    unlink_missing_ok('failed.endomill.ipynb')

    notebook_path \
        = f'{dirname(realpath(__file__))}/assets/instantiate_one_url.ipynb'
    os.environ['NOTEBOOK_PATH'] = notebook_path
    nb = nbformat.read(
        notebook_path,
        as_version=4,
    )
    client = NotebookClient(nb)
    client.execute()

    assert not exists('failed.endomill.ipynb')
    assert not exists('executing.endomill.ipynb')
    assert exists('parameter=https-example-com+ext=.endomill.ipynb')

    # post cleanup
    unlink_missing_ok('parameter=https-example-com+ext=.endomill.ipynb')


def test_intantiate_one_fail():
    # pre cleanup
    unlink_missing_ok('parameter=value+ext=.endomill.ipynb')
    unlink_missing_ok('executing.endomill.ipynb')
    unlink_missing_ok('failed.endomill.ipynb')

    notebook_path \
        = f'{dirname(realpath(__file__))}/assets/instantiate_one_fail.ipynb'
    os.environ['NOTEBOOK_PATH'] = notebook_path
    nb = nbformat.read(
        notebook_path,
        as_version=4,
    )
    client = NotebookClient(nb)
    client.execute()

    assert not exists('executing.endomill.ipynb')
    assert not exists('parameter=value+ext=.endomill.ipynb')
    assert exists('failed.endomill.ipynb')

    # post cleanup
    unlink_missing_ok('failed.endomill.ipynb')
