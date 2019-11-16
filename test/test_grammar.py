from unittest.mock import MagicMock

import pytest

from grammar import Alternation, Concatenation, List, Repetition, add_action, attribute

def test_alternation_append():
    alternation = Alternation()
    alternation.append('abc')
    assert alternation == Alternation('abc')

def test_concatenation_append():
    concatenation = Concatenation()
    concatenation.append('abc')
    assert concatenation == Concatenation('abc')

def test_list_single_item():
    assert List('abc', separator=',') == Concatenation('abc', Concatenation(',', 'abc').any)
    assert List('abc', separator=',').getters.get('__iter__')

def test_list_single_item_no_separator():
    assert List('abc') == Repetition.any('abc')

def test_list_multiple_items():
    items = Alternation('abc', 'def')
    assert List('abc', 'def', separator=',') == Concatenation(items, Concatenation(',', items).any)

def test_list_multiple_items_no_separator():
    assert List('abc', 'def') == Alternation('abc', 'def').any

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

def test_decorator_add_action():
    abc_def = Concatenation('abc', 'def')

    @add_action(abc_def)
    def _action(self):
        pass

    assert len(abc_def.actions) == 1
    assert abc_def.actions[0] == _action

def test_decorator_attribute():
    abc_def = Concatenation('abc', 'def')

    @attribute(abc_def)
    def first(self):
        return 42

    assert len(abc_def.getters) == 1
    assert abc_def.getters['first'] == first
    assert abc_def.first == 42

def test_decorator_attribute_cache():
    """ Test that the getter is called only once """
    abc_def = Concatenation('abc', 'def')

    mock_first = MagicMock()
    @attribute(abc_def)
    def first(self):
        mock_first()
        return 42

    assert len(abc_def.getters) == 1
    assert abc_def.getters['first'] == first
    assert abc_def.first == 42
    assert abc_def.first == 42
    mock_first.assert_called_once()
