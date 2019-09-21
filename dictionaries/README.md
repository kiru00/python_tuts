# About Dictionaries

Dictionaries are one of the most important and useful data structures in [Python][1].

In Python 3.5, dictionaries are still unordered, but this time, randomized data structures. This means that every time you re-run the dictionary, you’ll get a different items order.

In Python 3.6 and beyond, dictionaries are ordered data structures, which means that they keep their elements in the same order in which they were introduced.

They are mutable data structures. One can add, delete and update their items.

## Iterating through keys

Python’s dictionaries are mapping objects. This means that they inherit some special methods, which Python uses internally to perform some operations.

``` python
>>> dir({})
['__class__', '__contains__', '__delattr__', ... , '__iter__']
```
For mappings (like dictionaries), .__iter__() should iterate over the keys. This means that if you put a dictionary directly into a for loop, Python will automatically call .__iter__() on that dictionary, and you’ll get an iterator over its keys.

## ** Unpacking Operator

### Ref: dict_unpack.py

It’s important to note that if the dictionaries you’re trying to merge have repeated or common keys, then the values of the right-most dictionary will prevail

[ 1 ]: https://realpython.com/iterate-through-dictionary-python/
