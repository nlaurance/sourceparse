import unittest
import doctest


def test_doctests():
    # suite = unittest.TestSuite()
    # suite.addTest(doctest.DocFileSuite('../README.md'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    doctest.testfile('../README.md')

if __name__ == '__main__':
    test_doctests()
