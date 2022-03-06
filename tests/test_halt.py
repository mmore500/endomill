import nbformat
from nbclient import NotebookClient
from os.path import dirname, realpath


def test_in_interactive_notebook():
    nb = nbformat.read(
        f'{dirname(realpath(__file__))}/assets/halt.ipynb',
        as_version=4,
    )
    client = NotebookClient(nb)
    client.execute()
