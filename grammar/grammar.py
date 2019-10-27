_implicit_separator = None

class Base:
    def __init__(self):
        self.actions = []

    def add_action(self, callable):
        self.actions.append(callable)
        return self

class Repeatable:
    @property
    def any(self):
        return Repetition.any(self)

    @property
    def at_least(self, minimum):
        return Repetition.at_least(self, minimum)

    @property
    def one_or_more(self):
        return Repetition.one_or_more(self)

    @property
    def optional(self):
        return Repetition.optional(self)

class Alternation(Base, Repeatable):
    def __init__(self, *elements, ordered=False):
        super().__init__()
        self.elements = list(elements)
        self.ordered = ordered

    def __getitem__(self, key):
        return self.elements[key]

    def __eq__(self, other):
        if not isinstance(other, Alternation):
            return NotImplemented
        return self.elements == other.elements

    def append(self, item):
        return self.elements.append(item)

class Concatenation(Base, Repeatable):
    def __init__(self, *elements):
        super().__init__()
        self.elements = list(elements)

        # Capture the separator that was in effect at the time of construction
        self.separator = _implicit_separator

    def __getitem__(self, key):
        return self.elements[key]

    def __eq__(self, other):
        if not isinstance(other, Concatenation):
            return NotImplemented
        return self.elements == other.elements

    def __or__(self, other):
        return Alternation(self, other)

    def __ror__(self, other):
        return Alternation(other, self)

    def append(self, item):
        return self.elements.append(item)

class Repetition(Base):
    def __init__(self, element, maximum, minimum):
        super().__init__()
        self.element = element
        self.maximum = maximum
        self.minimum = minimum

    def __getitem__(self, key):
        return self.element[key]

    def __eq__(self, other):
        # Ignore unrelated types
        if not isinstance(other, Repetition):
            return NotImplemented
        return (self.element == other.element) and (self.maximum == other.maximum) and (self.minimum == other.minimum)

    def is_optional(self):
        return (self.maximum == 1) and (self.minimum == 0)

    @classmethod
    def any(cls, element):
        return cls(element, maximum=None, minimum=0)

    @classmethod
    def at_least(cls, element, minimum):
        return cls(element, maximum=None, minimum=minimum)

    @classmethod
    def one_or_more(cls, element):
        return cls.at_least(element, 1)

    @classmethod
    def optional(cls, element):
        return cls(element, maximum=1, minimum=0)

# ---

def add_action(pattern):
    """ A decorator for adding an action to a grammar-element """
    def decorator(func):
        pattern.add_action(func)
        return func

    return decorator

def implicit_separator(separator):
    """ Set the implicit separator that's assumed to be between every element of a Concatenation """
    global _implicit_separator
    _implicit_separator = separator
