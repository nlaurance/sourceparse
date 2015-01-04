sourceparse
===========

a personal adaptation of pyclbr from the standard python lib

let's say we want to analyze a source file like this one

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
...     def method2(self, foo, bar):
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

>>> from sourceparse import CodeCollector

for the purpose of this documentation we'll override the _readfile method

>>> def override(foo): return [s+'\n' for s in source.split('\n')]
...

>>> original = CodeCollector._readfile
>>> CodeCollector._readfile=override

let's instantiate a parser, normally we would pass a path to the file to analyze

>>> parser=CodeCollector("source")

first we need to parse the file

>>> parser.parse()

>>> parser.classes
[Class MixinUser: from 2 to 18
]

>>> parser.functions
[Function my_function: from 19 to 24
]




let's put the parser back to normal

>>> CodeCollector._readfile = original
