.. image:: https://img.shields.io/pypi/v/googlevoice.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/googlevoice.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/googlevoice

.. image:: https://dev.azure.com/jaraco/googlevoice/_apis/build/status/jaraco.googlevoice?branchName=master
   :target: https://dev.azure.com/jaraco/googlevoice/_build/latest?definitionId=1&branchName=master

.. image:: https://img.shields.io/travis/jaraco/googlevoice/master.svg
   :target: https://travis-ci.org/jaraco/googlevoice

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. image:: https://img.shields.io/appveyor/ci/jaraco/googlevoice/master.svg
   :target: https://ci.appveyor.com/project/jaraco/googlevoice/branch/master

.. image:: https://readthedocs.org/projects/googlevoice/badge/?version=latest
   :target: https://googlevoice.readthedocs.io/en/latest/?badge=latest


Python Google Voice Library

Based on pygooglevoice by Joe McCall & Justin Quick.

This project is *essentially broken* as the login API has changed and a new technique for logging in has not been developed. Please see `issue 8 <https://github.com/jaraco/googlevoice/issues/8>`_ for details.


Exposing the Google Voice "API" to the Python language
-------------------------------------------------------

Google Voice for Python Allows you to place calls, send sms, download voicemail, and check the various folders of your Google Voice Account.
You can use the Python API or command line script to schedule calls, check for new recieved calls/sms, or even sync your recorded voicemails/calls.
