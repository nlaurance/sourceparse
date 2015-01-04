""" main test module """
import os
import unittest
from sourceparse import CodeCollector


class TestParser(unittest.TestCase):

    def setUp(self):
        filename = os.path.join(os.path.dirname(__file__), 'lorem.py')
        self.parser = CodeCollector(filename)
        self.parser.parse()
        self.classes = self.parser.classes
        self.functions = self.parser.functions

    def testClasses(self):
        """ we find classes name
        """
        got = [c.name for c in self.classes]
        expected = ['Base', 'Sub1', 'MixinUser']
        self.assertEquals(got, expected)

    def testClassesLines(self):
        """ we find classes lines
        """
        got = [(c.from_line, c.to_line) for c in self.classes]
        expected = [(3, 9), (10, 13), (14, 27)]
        self.assertEquals(got, expected)

    def testClassesDecorators(self):
        """ we find classes decorators
        """
        got = [c.decorators for c in self.classes]
        expected = [['@decorated(somehow)\n', '@extra\n'], [], []]
        self.assertEquals(got, expected)

    def testFunctions(self):
        """ we find module functions name
        """
        got = [f.name for f in self.functions]
        expected = ['my_function', 'my_decorated_function']
        self.assertEquals(got, expected)

    def testFunctionsLines(self):
        """ we find functions lines
        """
        got = [(f.from_line, f.to_line) for f in self.functions]
        expected = [(28, 32), (34, 37)]
        self.assertEquals(got, expected)

    def testFunctionsDecorators(self):
        """ we find functions decorators
        """
        got = [f.decorators for f in self.functions]
        expected = [[], ['@deprecated\n']]
        self.assertEquals(got, expected)