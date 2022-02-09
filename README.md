# ponparse

Python Object Notation (PON) Parser

## What is it?

There is JSON for JavaScript Object Notation. Python can parse JSON files.

When Python prints an object tree of builtin types, it appears similar to JSON, but slightly different. What if you want to read the output of something that was printed by Python? The best existing option is ast.literal_eval(), which is a safe parser (will not run arbitrary code) and you should probably use that. But that can be slow, and for large strings it can overflow the stack. This project might eventually be better than that. For now it is beta software.

## Status

Currently it parses int, bool, str (but see limitations), float (including exponential notation, nan, and inf), None, list, dict, tuple.

## Limitations

Strings - Does not handle escaped characters, which is a pretty big gap for now. Does not handle double-quoted strings, which can be output in cases where the string contains single-quotes.

Does not parse set, byte, Ellipsis.

## Usage

Add it as a dependency. Then...

```python

>>> from ponparse import parse
>>> parse('3')
3
>>> x = parse('{1:[2,3]}')
>>> x
{1: [2, 3]}
>>> parse("{'a': nan}")
{'a': nan}
>>> parse("{'a': (nan, [2, None, (5, False)]), 4: -2.6e-34}")
{'a': (nan, [2, None, (5, False)]), 4: -2.6e-34}
