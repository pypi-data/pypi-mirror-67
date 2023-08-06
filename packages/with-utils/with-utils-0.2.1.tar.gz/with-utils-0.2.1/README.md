With Utils
==========

Utils that we've used a lot at WITH.

## `iter`

Iteration-related utils

### `n_grams`

Provides a way to create n_grams from an iterator

```python
from with_utils.iter import n_grams
assert list(n_grams([1, 2, 3, 4], 2)) == [(1, 2), (2, 3), (3, 4)]
```

### `return_list`

Transforms an iterator into a function that returns a list.

```python
from with_utils.iter import return_list

@return_list
def foo():
    yield 1
    yield 2
    yield 3

assert foo() == [1, 2, 3]
```
