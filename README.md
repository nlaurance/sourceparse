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
```python
>>> parser.classes
[Class MixinUser: from 2 to 18
]
```
each class
```python
>>> mix = parser.classes[0]
```
can list its methods
```python
>>> mix.methods
[Method method1: from 5 to 9
, Method method2: from 12 to 18
	decorated from 10 to 12]
```
each method
```python
>>> m2 = mix.methods[1]
```
has a name
```python
>>> m2.name
'method2'
```
a start line in the file
```python
>>> m2.from_line
12
```
an end line
```python
>>> m2.to_line
18
```
wa can access its docstring
```python
>>> m2.docstring
'method2 of MixinUser\n    '
```
decorators
```python
>>> m2.decorators
['    @manytimes\n', '    @decorated\n']
```
arguments, excluding self
```python
>>> m2.args
['foo', 'bar']
```
and its complete source, excluding decorators
```python
>>> pprint(m2.source)
['    def method2(self, foo, bar):\n',
 '        """ method2 of MixinUser\n',
 '        """\n',
 '        return\n',
 '\n',
 '# comment\n',
 '\n']
```
the module functions provide the same features
```python
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
```

let's put the parser back to normal
```python
>>> CodeCollector._readfile = original
```