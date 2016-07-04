========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |coveralls| |codecov|
        | |landscape| |scrutinizer|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/termquery/badge/?style=flat
    :target: https://readthedocs.org/projects/termquery
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/tomschr/termquery.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/tomschr/termquery

.. |coveralls| image:: https://coveralls.io/repos/tomschr/termquery/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/tomschr/termquery

.. |codecov| image:: https://codecov.io/github/tomschr/termquery/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/tomschr/termquery

.. |landscape| image:: https://landscape.io/github/tomschr/termquery/master/landscape.svg?style=flat
    :target: https://landscape.io/github/tomschr/termquery/master
    :alt: Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/termquery.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/termquery

.. |downloads| image:: https://img.shields.io/pypi/dm/termquery.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/termquery

.. |wheel| image:: https://img.shields.io/pypi/wheel/termquery.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/termquery

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/termquery.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/termquery

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/termquery.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/termquery

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/tomschr/termquery/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/tomschr/termquery/


.. end-badges

Terminology system

* Free software: BSD license

Installation
============

::

    pip install termquery

Documentation
=============

https://termquery.readthedocs.io/

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
