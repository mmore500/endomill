#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'IPython>=7.3.8',
    'keyname>=0.4.1',
    'nbmetalog>=0.2.5',
    'papermill[all]>=2.3.4',
    'python-slugify>=6.1.1',
]

setup_requirements = ['pytest-runner', ]

test_requirements = [
    'nbformat>=5.1.3',
    'nbmetalog>=0.2.5',
    'pytest>=3',
]

setup(
    author="Matthew Andres Moreno",
    author_email='m.more500@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description=(
        "endomill lets a Jupyter notebook instantiate itself as a papermill "
        "template"
    ),
    install_requires=requirements,
    license="MIT license",
    long_description_content_type="text/x-rst",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='endomill',
    name='endomill',
    packages=find_packages(include=['endomill', 'endomill.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mmore500/endomill',
    version='0.1.3',
    zip_safe=False,
)
