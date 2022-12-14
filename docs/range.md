# `GIter.range`

[< Back](./main.md)

## Signature

```py
range(stop: int, /) -> GIter[int]
range(start: int, stop: int, /) -> GIter[int]
range(start: int, stop: int, step: int, /) -> GIter[int]
```

## Details

Create an iterator given start*, stop and step* values. (\*: optional)

### Args

- start (int): start value of range (inclusive). Defaults to 0.
- stop (int | None, optional): stop value of range (exclusive).
- step (int, optional): step value of range. Defaults to 1, cannot be 0.

### Raises

- ValueError: if step equals 0.

> This method exists for completeness ; you probably want to use Python's built-in `range` instead.

## Examples

Using only `stop`:

```py
>>> for i in GIter.range(10):
...     print(i, end=" ")
0 1 2 3 4 5 6 7 8 9
```

Using `start` and `stop`:

```py
>>> for i in GIter.range(3, 7):
...     print(i, end=" ")
3 4 5 6
```

Using `start`, `stop` and `step`:

```py
>>> for i in GIter.range(1, 12, 2):
...     print(i, end=" ")
1 3 5 7 9 11
```
