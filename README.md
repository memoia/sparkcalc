sparkcalc
=========

Summary
-------

Write a calculator _library_.

Requirements:

* Handle binary operations, e.g. 5 ­ 6, 8 * 4
* The calculator should be able to handle a full arithmetic
  expression at once, for example: 1 + 1 ­ 4 * 4
* The library must take
  [Order of Operations](http://en.wikipedia.org/wiki/Order_of_operations)
  into account
* No need to handle parentheses, e.g. (1 + 1 ­ 4) * 4
* Must be *extendable* so that it accepts user­defined operands

Objectives:

* OOP
* Best practices
* Algorithms


Thoughts
--------

Need to convert infix notation into a tree or find another alternative.
Dijkstra's shunting yard method can be used here; it might be shorter to
convert to RPN instead and process a stack than build and traverse a tree.

From an OOP perspective, we might consider operators to be tokenized into
a subclass of a general "Operator", each having specific attributes regarding
symbol and precedence/weight, etc. From a practical perspective, this might
be overkill.

For simplicity's sake, let's assume that we'll only accept positive
integers.

In addition to listed requirements, library should be self-contained
for ease of demonstration/review.

Choosing Python to solve problem since it is great for modeling concepts.
The runtime environment also comes with a built-in unit test library, making
it easy to show that the project works (and doesn't work) under various
scenarios.


Using it
--------

Assumes Python 2.7 is installed and available in the PATH. Assumes GNU
Make is installed.

Run ``make`` to execute tests/demos.
