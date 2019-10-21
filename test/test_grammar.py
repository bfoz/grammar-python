import pytest

from grammar import Alternation, Concatenation, Repetition

def test_alternation_append():
    alternation = Alternation()
    alternation.append('abc')
    assert alternation == Alternation('abc')

def test_concatenation_append():
    concatenation = Concatenation()
    concatenation.append('abc')
    assert concatenation == Concatenation('abc')

def test_repetition_attributes():
    assert Repetition('abc', 42, 24).element == 'abc'
    assert Repetition('abc', 42, 24).maximum == 42
    assert Repetition('abc', 24, 42).minimum == 42

def test_repetition_any():
    assert Repetition.any('abc') == Repetition('abc', None, 0)

def test_repetition_at_least():
    assert Repetition.at_least('abc', 5) == Repetition('abc', None, 5)

def test_repetition_one_or_more():
    assert Repetition.one_or_more('abc') == Repetition('abc', None, 1)

def test_repetition_optional():
    assert Repetition.optional('abc') == Repetition('abc', 1, 0)
