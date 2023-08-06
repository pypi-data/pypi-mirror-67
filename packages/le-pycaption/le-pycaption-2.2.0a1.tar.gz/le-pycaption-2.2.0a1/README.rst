pycaption
==========

|Build Status|

**PLEASE SEE** `pbs/pycaption <https://github.com/pbs/pycaption>`__ **FOR OFFICIAL RELEASES.**

``pycaption`` is a caption reading/writing module. Use one of the given Readers
to read content into a CaptionSet object, and then use one of the Writers to
output the CaptionSet into captions of your desired format.

Version 2.0.0\@learningequality passes all tests with Python 2.7, 3.4, 3.5, 3.6, and 3.7.

For details, see the `documentation <http://pycaption.readthedocs.org>`__.

Changelog
---------

2.2.0\@learningequality
^^^^^^^^^^^^^^^^^^^^^^^
- Added ``enum_compat`` library to maintain Python 2.7 support
- Pinned ``beautifulsoup4`` under ``v4.9.0`` as it caused numerous test failures
- Unpinned ``lxml``
- Misc Travis and Tox updates

2.0.0\@learningequality
^^^^^^^^^^^^^^^^^^^^^^^
- Python 2 and 3 support (see branch `py27\@pbs <https://github.com/pbs/pycaption/tree/py27>`__)
- Upgraded ``beautifulsoup4`` package to a more current version, and resolved issues with tests due to upgrade. See full detailed changes `here <https://github.com/learningequality/pycaption/pull/1>`__.
- Removed ``from future import standard_library`` as it can cause issues with other packages and its removal causes no test failures.
- Fixed ``DFXPReader`` issue with default language (see `this PR <https://github.com/pbs/pycaption/pull/188>`__)
- Changed global default language to ISO-639-2 undetermined language code ``und`` (see `this PR <https://github.com/pbs/pycaption/pull/188>`__)

1.0.0\@pbs
^^^^^^^^^^
- Added Python 3 support (see `pbs/pycaption <https://github.com/pbs/pycaption>`__).

0.5.x\@pbs
^^^^^^^^^^
- Added positioning support
- Created documentation

License
-------

This module is Copyright 2012 PBS.org and is available under the `Apache
License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`__.

.. |Build Status| image:: https://travis-ci.org/pbs/pycaption.png?branch=master
   :target: https://travis-ci.org/pbs/pycaption
