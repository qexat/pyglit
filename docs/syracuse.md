# `GIter.syracuse`

[< Back](./main.md)

## Signature

```py
syracuse(starting: int) -> GIter[int]
syracuse(starting: int, *, include_starting: bool) -> GIter[int]
```

## Details

Create an iterator of all the integers that follow `starting` in the Syracuse sequence according to the [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture).

### Args

- starting (int): the integer to start from.
- include_starting (bool, optional): whether the starting integer should be included. Defaults to False.

### Raises

- ValueError: if the starting integer is not positive.

## Examples

```py
>>> for n in GIter.syracuse(15):
...     print(n)
46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1
```
