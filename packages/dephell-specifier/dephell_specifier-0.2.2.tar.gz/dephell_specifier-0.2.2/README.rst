
Dephell Specifier
-----------------


.. image:: https://travis-ci.org/dephell/dephell_specifier.svg?branch=master
   :target: https://travis-ci.org/dephell/dephell_specifier
   :alt: travis


.. image:: https://ci.appveyor.com/api/projects/status/github/dephell/dephell_specifier?svg=true
   :target: https://ci.appveyor.com/project/orsinium/dephell-specifier
   :alt: appveyor


.. image:: https://img.shields.io/pypi/l/dephell-specifier.svg
   :target: https://github.com/dephell/dephell_specifier/blob/master/LICENSE
   :alt: MIT License


Work with version specifiers.

Supported specifiers:


* `PEP-440 <https://www.python.org/dev/peps/pep-0440/>`_.
* `NPM SemVer <https://github.com/npm/node-semver>`_.
* `Maven <http://maven.apache.org/enforcer/enforcer-rules/versionRanges.html>`_.
* `RubyGems <https://guides.rubygems.org/patterns/>`_

Installation
------------

Install from `PyPI <https://pypi.org/project/dephell-specifier/>`_\ :

.. code-block:: bash

   python3 -m pip install --user dephell_specifier

Usage
-----

.. code-block:: python

   from dephell_specifier import RangeSpecifier

   '3.4' in RangeSpecifier('*')
   # True

   '3.4' in RangeSpecifier('<=2.7')
   # False

   '3.4' in RangeSpecifier('>2.7')
   # True

   '3.4' in RangeSpecifier('>2.7,<=3.4')
   # True

   '3.4' in RangeSpecifier('<2.7 || >=3.4')
   # True
