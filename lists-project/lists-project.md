# Project: Lists

In this project, you will implement a List class in four different ways, and one test suite that thoroughly tests a given List class. The same test suite must work for all four implementations. Make sure that your test suite is sufficiently comprehensive to offer good confidence in the correctness of your implementations.

*Note: do not confuse List (the class that you will implement) with `list` (the built-in class).*

See `timeofday.py` for an example of the general structure of what your solution should look like, but applied to a TimeOfDay class rather than a List class.

Each of your four List implementations will define exactly the same methods, and these methods shall have exactly the same behavior, as far as client code can tell. The only difference between the implementations will be the way the elements are stored (which will also affect the performance of the various operations).

Each implementation shall define the following methods:

- A constructor that optionally takes a tuple with the initial elements of the List object. If a tuple is provided as an argument, then method `all_elements` shall initially return a tuple that is equal to this argument. If no argument is provided, the List object shall initially be empty (i.e. its length shall be 0 and `all_elements` shall return an empty tuple).

- A method `length` that returns the number of elements of `self` as an `int`. This is always equal to the length of the tuple returned by `all_elements`.

- A method `all_elements` that returns the elements of `self` as a tuple.

- A method `element_at_index` that takes an index (an `int` not less than 0 but less than the current length) and returns the element at that index. This is always equal to the element at this index in the tuple returned by `all_elements`.

- A method `insert_at_index` that takes an index (an `int` not less than 0 and not greater than the current length; it may be equal to the current length) and a value to insert, and inserts the given value at the given index. If before calling this method, `all_elements` returns a tuple `elems`, then after calling this method, `all_elements` returns `elems[:index] + (value,) + elems[index:]`.

- A method `remove_at_index` that takes an index (an `int` not less than 0 and less than the current length) and removes the element at the given index. If before calling this method, `all_elements` returns a tuple `elems`, then after calling this method, `all_elements` returns `elems[:index] + elems[index + 1:]`.

You shall implement this class in the following four ways:

## Implementation 1: using a list object

In this implementation, your class shall use a single attribute called `_elements` that refers to a `list` object that stores the elements.

## Implementation 2: using a singly linked list

In this implementation, your class shall use a single attribute called `_first_node` that is either `None` (if there are no elements) or a reference to the first object in a chain of `Node` objects that together store the elements.

A singly linked list that stores the values 10, 20, 30 can be constructed as follows:

```python
class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

linked_list = Node(10, Node(20, Node(30, None)))
```

Hint: use the following helper functions (where you need to replace the `...` by appropriate Python code):

```python
def linked_list_length(node):
    if ...:
        return ...
    else:
        return ... + linked_list_length(node.next)

def linked_list_all_elements(node):
    if ...:
        return ...
    else:
        return ... + linked_list_all_elements(node.next)

def linked_list_element_at_index(node, index):
    if ...:
        return ...
    else:
        return linked_list_element_at_index(node.next, index - 1)

def linked_list_insert_at_index(node, index, value):
    if ...:
        ...
    else:
        return linked_list_insert_at_index(node.next, index - 1, value)

def linked_list_remove_at_index(node, index):
    if ...:
        ...
    else:
        return linked_list_remove_at_index(node.next, index - 1)
```

## Implementation 3: using a doubly linked list

In this implementation, your class shall use an attribute `_length` and an attribute `_sentinel`, where the latter refers to the sentinel node of a cyclic doubly linked list with sentinel. The value of the `_length` attribute shall always be equal to the number of nodes in the doubly linked list, not counting the sentinel node.

A cyclic doubly linked list with sentinel that stores the values 10, 20, 30 can be constructed as follows:

```python
class Node:
    pass

sentinel = Node()
node1 = Node()
node2 = Node()
node3 = Node()

sentinel.next = node1
node1.previous = sentinel
node1.value = 10
node1.next = node2
node2.previous = node1
node2.value = 20
node2.next = node3
node3.previous = node2
node3.value = 30
node3.next = sentinel
sentinel.previous = node3
```

A cyclic doubly linked list with sentinel with no elements consists solely of a sentinel node that refers to itself:

```python
sentinel = Node()
sentinel.next = sentinel
sentinel.previous = sentinel
```

Notice that you can easily traverse a doubly linked list forwards, but also backwards. Use this property to optimize performance: to reach a node at an index I, check whether the index is closer to the start (i.e. I is less than half of the length) or closer to the end (i.e. I is not less than half of the length).

This way, make sure the time taken by your implementation's `element_at_index`, `insert_at_index`, and `remove_at_index` methods is independent of the length L given a fixed index I or given an index of the form L - K with K fixed (i.e. at a fixed distance from the start or end).

## Implementation 4: using a ring buffer

In this implementation, your class shall use an attribute `_buffer` that refers to a `list` object, an attribute `_start` that stores an `int` value not less than zero but less than the length of `_buffer`, and an attribute `_length` that stores an `int` value not less than zero and not greater than the length of `_buffer`. Initially, `_buffer` shall be a `list` object of length 10 whose elements are all `None`, and `_start` and `_length` are both 0. The implementation of method `all_elements` shall be as follows:

```python
def all_elements(self):
    return tuple(self._buffer[(self._start + i) % len(self._buffer)] for i in range(self._length))
```

The time required by your `insert_at_index` and `remove_at_index` methods shall be independent of the length, provided that the index is at a fixed distance from the start or end and that the buffer has free space. If the buffer is full, double its size.
