# Grammar

This is an attempt to make a cross-parser grammar specification for parsers written in Python. The result is a very opinionated module that is cranky about the sad state of grammar languages. _Grammar_ doesn't have a grammar file format, or even care what grammar file you use, so long as it can be translated into Grammar objects. The Grammar object hierarchy attempts to support all of the features supported by all of the major parsers. If you create a grammar using features that aren't supported by your favorite parser, then it's up to that parser to complain about the grammar that you tried to feed it.

_Grammar_ doesn't attempt to mitigate left-recursive alternations; a parser is expected to either handle the grammar properly, or to report an appropriate error for any grammar element that it can't handle.

## Grammars are Modules

Grammars are Modules, and the grammar rules are symbols defined in the grammar module.

The grammar module must define a method named `root` that returns the grammar's root rule.

```python
from grammar import Alternation, Concatenation, Repetition

def root():
    """ The name of the root rule of the grammar """
    return my_root_rule
```

## Rules

In _grammar_ rules are composed of _Alternations_, _Concatenations_, _Repetitions_, Strings, and Python regular expression objects.

Strings match themselves, and regular expressions match whatever they match. _Alternations_ match the longest of their alternations, _Concatenations_ match their elements in order, and _Repetitions_ match some number of something else.

```python
choice = Alternation('abc', 'def', 'xyz')		# Matches one of "abc", or "def", or "xyz"
concatenated = Concatenation('abc', 'def', 'xyz')	# Matches "abcdefxyz"
Repetition.any(choice)					# Matches any number of "abc", or "def", or "xyz"
```

### Repetitions

Repetitions are used extensively in many grammars and the syntax above can be rather unwieldy, even when used sparingly. To make things easier, the rule objects created by both `Alternation()` and `Concatenation()` have convenience methods for creating repetitions of the underlying grammar elements

```python
choice = Alternation('abc', 'def', 'xyz')

choice.any		# Matches any number of "abc", or "def", or "xyz"
choice.at_least(2) 	# Matches 2, or more, of "abc", or "def", or "xyz"
choice.one_or_more 	# Equivalent to choice.at_least(1)
choice.optional 	# Matches one of, or none of, "abc", or "def", or "xyz"

```
