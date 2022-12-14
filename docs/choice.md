# `GIter.choice`

[< Back](./main.md)

## Signature

```py
choice(seq: Sequence[T_co]) -> GIter[T_co]
choice(seq: Sequence[T_co], *, consume: bool = True) -> GIter[T_co]
choice(seq: Sequence[T_co], *, consume: bool, max_size: int) -> GIter[T_co]
```

## Details

Create an iterator from a sequence that yields randomly an element.
By default, consumes this latter ; this can be set off, which would make the iterator infinite except if you set a maximum size.

### Args

- seq (Sequence[T]): the sequence used to build the iterator.
- consume (bool, optional): if the picked elements are popped off the iterator. Defaults to True.
- max_size (int, optional): sets the iterator max size (useful if `consume` is set to False). Defaults to None.

> Remember when you learned probability in high school using bags filled with balls? That's basically that :D

## Examples

Let's say that we have a bag filled with numbered balls.
We want to pick a ball out ten times, putting them back afterward:

```py
>>> l = [3, 5, 2, 1]
>>> for i in GIter.from_choice(l, consume=False, max_size=10):
...     print(i, end=" ")
1 2 1 1 2 2 3 5 3 2
```

Same scenario, but we don't put the balls back:

```py
>>> l = [3, 5, 2, 1]
>>> for i in GIter.from_choice(l, max_size=10):
...     print(i, end=" ")
1 5 2 3
```
