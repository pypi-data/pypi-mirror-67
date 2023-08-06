JMESObj Lightweight Data Container
----------------------------------

This project contains a class with index-like JMESPath querying.

Example::

  >>> from jmesobj import JMESObj
  >>> obj = JMESObj.from_json('{"foo": {"bar": true, "baz": false}}')
  >>> obj['foo.bar']
  True
  >>> obj['foo.*']
  [True, False]

Installation
============

Using ``pip``::

  $ pip install jmesobj


Development
===========

Development environment is set up by ``pipenv``::

  $ pipenv install --dev
