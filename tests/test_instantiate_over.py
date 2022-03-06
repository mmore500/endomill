import nbformat
from nbclient import NotebookClient
import os
from os.path import dirname, exists, realpath

from endomill._unlink_missing_ok import unlink_missing_ok


def test_intantiate_over():
    expected_outputs = [
        'parameter=value1+ext=.endomill.ipynb',
        'parameter=value2+ext=.endomill.ipynb',
    ]

    # pre cleanup
    unlink_missing_ok('executing.endomill.ipynb')
    unlink_missing_ok('failed.endomill.ipynb')
    for expected_output in expected_outputs:
        unlink_missing_ok(expected_output)

    notebook_path \
        = f'{dirname(realpath(__file__))}/assets/instantiate_over.ipynb'
    os.environ['NOTEBOOK_PATH'] = notebook_path
    nb = nbformat.read(
        notebook_path,
        as_version=4,
    )
    client = NotebookClient(nb)
    client.execute()

    assert not exists('failed.endomill.ipynb')
    assert not exists('executing.endomill.ipynb')
    for expected_output in expected_outputs:
        assert exists(expected_output)

    # post cleanup
    for expected_output in expected_outputs:
        unlink_missing_ok(expected_output)


def test_intantiate_over_fai():
    expected_outputs = [
        'parameter=value1+ext=.endomill.ipynb',
        'parameter=value2+ext=.endomill.ipynb',
    ]

    # pre cleanup
    unlink_missing_ok('executing.endomill.ipynb')
    unlink_missing_ok('failed.endomill.ipynb')
    for expected_output in expected_outputs:
        unlink_missing_ok(expected_output)

    notebook_path \
        = f'{dirname(realpath(__file__))}/assets/instantiate_over_fail.ipynb'
    os.environ['NOTEBOOK_PATH'] = notebook_path
    nb = nbformat.read(
        notebook_path,
        as_version=4,
    )
    client = NotebookClient(nb)
    client.execute()

    assert not exists('executing.endomill.ipynb')
    assert exists('failed.endomill.ipynb')
    for expected_output in expected_outputs:
        assert not exists(expected_output)

    # post cleanup
    unlink_missing_ok('failed.endomill.ipynb')
