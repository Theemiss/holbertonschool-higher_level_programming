The ``text_indentation`` module
======================

using ``text_indentation()``

----------------------

Testing import import text_indentation:
    >>> text_indentation = __import__('5-text_indentation').text_indentation

test normal:
    >>> text_indentation("test? azer")
    test?
    <BLANKLINE>
    azer

test text not str
    >>> text_indentation(5)
    Traceback (most recent call last):
    ...
    TypeError: text must be a string

test output
    >>> text_indentation("Lorem? ipsum dolor sit amet, consectetur adipiscing elit.")
    Lorem?
    <BLANKLINE>
    ipsum dolor sit amet, consectetur adipiscing elit.
    <BLANKLINE>

Testing missing args
    >>> text_indentation()
    Traceback (most recent call last):
    ...
    TypeError: text_indentation() missing 1 required positional argument: 'text'
