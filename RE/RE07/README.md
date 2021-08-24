## Assignment #7: Tuples

### 1. Unique

Write a Python function `unique(atuple)` that receives a tuple of integers and returns a tuple with the sorted unique elements of the tuple.

Save the program in the file [unique.py](unique.py).

For example:

- for `atuple=(8, 8, 1, 3, 1, 3, 5)` the function returns the tuple `(1, 3, 5, 8)`
- for `atuple=(1, 1, 1, 1)` the function returns the tuple `(1,)`

**Hint:** For sorting, you may use the built-in function `sorted()`

### 2.  Find my Type

Write a Python function `find_dtype(atuple, data_type)` that, given a tuple atuple, returns another tuple containing just the elements of type data_type. It should be assumed that data_type is a string with one of the following values: `int`, `float`, `complex`, `bool`, `str` or `tuple`.

Save the program in the file [find_dtype.py](find_dtype.py).

For example:

- for `atuple=(1, False, "hello", 2., "world")` and `data_type="str"`, the function returns the tuple `("hello", "world")`
- for `atuple=(1, 2, 3)` and `data_type="float"`, the function returns the empty tuple `()`

**Hint:** Look at `__name__` in the Python Standard Library

### 3. Translation table

Write a Python function `translate(astring, table)` that translates a given string *astring* using a translation table.

The translation table, table, is a nested tuple with an arbitrary number of translation pairs/tuples (in_value, out_value).

Save the program in the file [translate.py](translate.py)

For example:

- for `astring="Hello world!"` and `table=(('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5), ('!', ' :)'))`, the function returns the string `H2ll4 w4rld :)`
- for astring="Testing this string..." and table=((' ', '--'), ('.', '!'), ('i', 'o'), ('t', 'tt')), the function returns the string "Testtong--tthos--sttrong!!!" (without quotes)

### 4. Zero-sum Triplet

Given a tuple of n integers, with n > 3, write a Python function triplet(atuple) that finds a triplet (a, b, c) such that their sum is zero (i.e., a + b + c = 0).

In case there is more than one triplet that sums up to zero, you should return the triplet with the lowest index (idx), such that (idx a , idx b, idx c ) < (idx an , idx bn, idx cn ). In case there are no triplets that sum up to zero, you should return an empty tuple ().

Save the program in the file [triplet.py](triplet.py).

For example:

- for atuple=(-8, 0, 4, -2, -1, 1, 2), the function returns the tuple (0, -2,
2)
- for atuple=(-1, 1, 1, 1), the function returns the tuple ()
- for atuple=(-4, 3, 0, -2, -1, -3), the function returns the tuple (3, 0, -3)