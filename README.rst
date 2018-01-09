.. image:: https://travis-ci.org/nlaurance/sourceparse.svg?branch=master
    :target: https://travis-ci.org/nlaurance/sourceparse
    :alt: Build Status

.. image:: https://readthedocs.org/projects/sourceparse/badge/?version=latest
    :target: https://readthedocs.org/projects/sourceparse/?badge=latest
    :alt: Documentation Status

.. image:: https://coveralls.io/repos/nlaurance/sourceparse/badge.svg
    :target: https://coveralls.io/r/nlaurance/sourceparse


sourceparse
===========

A personal adaptation of ``pyclbr`` from the standard Python library.

Let's say we want to analyze a source file like this one:

.. code-block:: python

    >>> source = '''
    ... class MixinUser(Sub2, Mixin):
    ...     """Overrides method1 and method2
    ...     """
    ...
    ...     def method1(self, foo):
    ...         """ method1 of MixinUser
    ...         """
    ...         return
    ...
    ...     @manytimes
    ...     @decorated
    ...     def method2(self, foo, bar=None):
    ...         """ method2 of MixinUser
    ...         """
    ...         return
    ...
    ... # comment
    ...
    ... def my_function(foo):
    ...     """ Stand-alone function.
    ...     """
    ...     return
    ... '''

Of course, we'll start by importing the tool:

.. code-block:: python

    >>> from sourceparse import CodeCollector
    >>> from pprint import pprint

For the purpose of this documentation, we'll override the ``_readfile`` method:

.. code-block:: python

    >>> def override(foo): return [s+'\n' for s in source.split('\n')]
    ...
    >>> original = CodeCollector._readfile
    >>> CodeCollector._readfile=override



Instantiation
-------------

Let's instantiate a parser. Normally, we would pass in a path to the file we wish to analyze:

.. code-block:: python

    >>> parser=CodeCollector("source")

Access to Members
-----------------

Classes
~~~~~~~

We can now access a list of the classes defined in the module:

.. code-block:: python

    >>> parser.classes
    [Class MixinUser: from 2 to 19
    ]


Methods
~~~~~~~

Each class:

.. code-block:: python

    >>> mix = parser.classes[0]

Can list its methods:

.. code-block:: python

    >>> mix.methods
    [Method method1: from 6 to 10
    , Method method2: from 13 to 19
    	decorated from 11 to 13]

Each method:

.. code-block:: python

    >>> m2 = mix.methods[1]

Has a name:

.. code-block:: python

    >>> m2.name
    'method2'

A start line in the file:

.. code-block:: python

    >>> m2.from_line
    13


An end line:

.. code-block:: python

    >>> m2.to_line
    19

We can access its docstring:

.. code-block:: python

    >>> m2.docstring
    'method2 of MixinUser\n    '

Decorators:

.. code-block:: python

    >>> m2.decorators
    ['    @manytimes\n', '    @decorated\n']

Arguments, excluding self:

.. code-block:: python

    >>> m2.args
    ['foo']

Keyword arguments:

.. code-block:: python

    >>> m2.kwargs
    {'bar': 'None'}

Its complete source, excluding decorators:

.. code-block:: python

    >>> pprint(m2.source)
    ['    def method2(self, foo, bar=None):\n',
     '        """ method2 of MixinUser\n',
     '        """\n',
     '        return\n',
     '\n',
     '# comment\n',
     '\n']

.. note:: The inline comment at the same level is included.

Functions
~~~~~~~~~

The module functions provide the same features:

.. code-block:: python

    >>> parser.functions
    [Function my_function: from 20 to 24
    ]
    >>> my = parser.functions[0]
    >>> my.decorators
    []
    >>> my.docstring
    'Stand-alone function.\n    '
    >>> my.args
    ['foo']

    >>> my.from_line
    20
    >>> my.to_line
    24
    >>> pprint(my.source)
    ['def my_function(foo):\n',
     '    """ Stand-alone function.\n',
     '    """\n',
     '    return\n',
     '\n']

Let's reset the parser back to normal:

.. code-block:: python

>>> CodeCollector._readfile = original


Links
~~~~~

* Source: https://github.com/nlaurance/sourceparse
* Doc: http://sourceparse.readthedocs.org/
