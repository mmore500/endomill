========
endomill
========


.. image:: https://img.shields.io/pypi/v/endomill.svg
        :target: https://pypi.python.org/pypi/endomill

.. image:: https://img.shields.io/travis/mmore500/endomill.svg
        :target: https://travis-ci.com/mmore500/endomill

.. image:: https://readthedocs.org/projects/endomill/badge/?version=latest
        :target: https://endomill.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




endomill lets a Jupyter notebook instantiate itself as a papermill template.

Plays nice across both interactive and automatic (i.e., nbconvert, nbclient) contexts.


* Free software: MIT license
* Documentation: https://endomill.readthedocs.io.


Here's what cells from a notebook using endomill might look like.

.. code-block:: python3

  import endomill


Instantiate & execute this two copies of this notebook.

.. code-block:: python3

  endomill.instantiate_over(
      parameter_packs=[
          {'parameter' : 'value1'},
          {'parameter' : 'value2'},
      ],
  )


Supply papermill parameters.
(Remember to add notebook cell "parameters" tag for papermill.)

.. code-block:: python3

  # register papermill parameters
  parameter: str


Override automatic endomill instance output path, if desired.

.. code-block:: python3

  endomill.add_instance_outpath('custom_outpath.endomill.ipynb')


Then do your Jupyter business as usual!

.. code-block:: python3

  print('hello', parameter)


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
