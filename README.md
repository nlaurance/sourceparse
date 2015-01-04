sourceparse
===========

a personal adaptation of pyclbr from the standard python lib

let's say we want to analyze a source file like this one
```python
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
```

```python
>>> from sourceparse import CodeCollector
>>> from pprint import pprint
```

for the purpose of this documentation we'll override the _readfile method

```python
>>> def override(foo): return [s+'\n' for s in source.split('\n')]
...
>>> original = CodeCollector._readfile
>>> CodeCollector._readfile=override
```

let's instantiate a parser, normally we would pass a path to the file to analyze

```python
>>> parser=CodeCollector("source")
```

first we need to parse the file
```python
>>> parser.parse()
```

we can now access a list of the classes defined in the module
>>> parser.classes
[Class MixinUser: from 2 to 18
]

each class
>>> mix = parser.classes[0]

can list its methods
>>> mix.methods
[Method method1: from 5 to 9
, Method method2: from 12 to 18
	decorated from 10 to 12]

each method
>>> m2 = mix.methods[1]

has a name
>>> m2.name
'method2'

a start line in the file
>>> m2.from_line
12

an end line
>>> m2.to_line
18

wa can access its docstring
>>> m2.docstring
'method2 of MixinUser\n    '

decorators
>>> m2.decorators
['    @manytimes\n', '    @decorated\n']

arguments, excluding self
>>> m2.args
['foo', 'bar']

and its complete source, excluding decorators
>>> pprint(m2.source)
['    def method2(self, foo, bar):\n',
 '        """ method2 of MixinUser\n',
 '        """\n',
 '        return\n',
 '\n',
 '# comment\n',
 '\n']

the module functions provide the same features
>>> parser.functions
[Function my_function: from 19 to 24
]
>>> my = parser.functions[0]
>>> my.decorators
[]
>>> my.docstring
'Stand-alone function.\n    '
>>> my.args
['foo']

>>> my.from_line
19
>>> my.to_line
24
>>> pprint(my.source)
['def my_function(foo):\n',
 '    """ Stand-alone function.\n',
 '    """\n',
 '    return\n',
 '    \n',
 '\n']


let's put the parser back to normal
```python
>>> CodeCollector._readfile = original
```