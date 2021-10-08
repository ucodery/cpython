import doctest
import unittest


doctests = """
########### Tests mostly copied from test_listcomps.py ############

Test basic reflection

    >>> foo = <<<
    >>> foo
    'foo'

Test expression reflection

    >>> if foo := <<<: foo
    'foo'

Test reflection as argument

    >>> foo = str.capitalize(<<<)
    >>> foo
    'Foo'

Test multi-assignment on same line

    >>> bar = foo = <<<
    >>> bar
    'foo'

Test multi-target on same line

    >>> bar, foo = <<<, 'other'
    >>> bar
    'foo'

Test assignment statement and expression

    >>> bar = str(object := <<<)
    >>> bar
    'object'

Test dict lookup

    >>> d = {'foo': 'cheese', 'bar': 'spam'}
    >>> if foo := d.get(<<<):
    ...     if bar := d.get(<<<):
    ...         foo + ' and ' + bar
    'cheese and spam'

Test namedtuple

    >>> from collections import namedtuple
    >>> Point = namedtuple(<<<, ['x', 'y'])
    >>> Point(1, 2)
    Point(x=1, y=2)

Test Enum

    >>> from enum import Enum
    >>> class Color(Enum):
    ...     RED = <<<
    ...     GREEN = <<<
    ...     BLUE = <<<
    >>> Color.RED.value
    'RED'

Test make_dataclass

    >>> from dataclasses import make_dataclass
    >>> Window = make_dataclass(<<<, [('width', int), ('height', int)])
    >>> Window
    <class 'types.Window'>

Test NewType

    >>> from typing import TypeVar
    >>> T = TypeVar(<<<)
    >>> T
    ~T

Test outside of assignment

    >>> print(<<<)
    Traceback (most recent call last):
    ...
    SyntaxError: <<< can only be used in assignment statements

"""


__test__ = {'doctests' : doctests}

def load_tests(loader, tests, pattern):
    tests.addTest(doctest.DocTestSuite())
    return tests


if __name__ == "__main__":
    unittest.main()
