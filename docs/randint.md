# `GIter.randint`

[< Back](./main.md)

## Signature

```py
random(int_min: int, int_max: int) -> GIter[int]
random(int_min: int, int_max: int, *, iterations: int) -> GIter[int]
```

## Details

Create an iterator of random integers.

### Args

- int_min (int): the minimum integer value (`randint`'s `a`).
- int_max (int): the maximum integer value (`randint`'s `b`).
- iterations (int | None, optional): number of iterations. If not specified, the iterator is infinite. Defaults to None.

### Raises

- ValueError: if `int_min` is bigger than `int_max`.

## Examples

Making a simulation of three independent dice rolls:

```py
>>> for roll in GIter.randint(1, 6, iterations=3):
...     print(roll)
4
2
1
```
