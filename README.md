# Pyglit (PYthon GLeam ITerator)

On its core, it's inspired from [Gleam](https://github.com/gleam-lang/gleam)'s iterator (hence the name).

It's more like a PoC rather than an actual module ; the idea is to experiment on how this could be used
in the wild, and if it is conclusive, then to build an actual project to publish on PyPI.

## Documentation

You can find some documentation [here](./docs/main.md).

## Some examples

```py
# Importing the iterator
>>> from pyglit import GIter

# Generating 5 random numbers
>>> for x in GIter.random(iterations=5):
...    print(x, end=" ")
0.3055292429351516
0.36749204105856714
0.6805446569793817
0.7202938729506683
0.32271912974934525

# Picking 5 times a ball from the bag `l`
>>> l = ["red", "blue"]
>>> for ball in GIter.choice(l, consume=False, max_size=5):
...     print(ball)
red
blue
blue
blue
red

# Getting the Syracuse sequence with u0 = 5
>>> for n in GIter.syracuse(5, include_starting=True):
...     print(n)
5
16
8
4
2
1
```
