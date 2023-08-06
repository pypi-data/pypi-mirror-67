========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/spwla/badge/?style=flat
    :target: https://readthedocs.org/projects/spwla
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/lianglin0310/spwla.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/lianglin0310/spwla

.. |requires| image:: https://requires.io/github/lianglin0310/spwla/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/lianglin0310/spwla/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/lianglin0310/spwla/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/lianglin0310/spwla

.. |version| image:: https://img.shields.io/pypi/v/spwla.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/spwla

.. |wheel| image:: https://img.shields.io/pypi/wheel/spwla.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/spwla

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/spwla.svg
    :alt: Supported versions
    :target: https://pypi.org/project/spwla

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/spwla.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/spwla

.. |commits-since| image:: https://img.shields.io/github/commits-since/lianglin0310/spwla/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/lianglin0310/spwla/compare/v0.0.0...master



.. end-badges

A Python package by SPWLA for educational purpose

* Free software: MIT license

Installation
============

::

    pip install spwla

You can also install the in-development version with::

    pip install https://github.com/lianglin0310/spwla/archive/master.zip


Documentation
=============


https://spwla.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
