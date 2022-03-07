"""Top-level package for endomill."""

__author__ = """Matthew Andres Moreno"""
__email__ = 'm.more500@gmail.com'
__version__ = '0.1.3'

from .add_instance_outpath import add_instance_outpath
from .in_interactive_notebook import in_interactive_notebook
from .instantiate_one import instantiate_one
from .instantiate_over import instantiate_over

# adapted from https://stackoverflow.com/a/31079085
__all__ = [
    'add_instance_outpath',
    'in_interactive_notebook',
    'instantiate_one',
    'instantiate_over',
]
