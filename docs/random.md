# `GIter.random`

[< Back](./main.md)

## Signature

```py
random() -> GIter[float]
random(*, iterations: int) -> GIter[float]
random(min: float, max: float) -> GIter[float]
random(min: float, max: float, *, iterations: int) -> GIter[float]
```

## Details

Create an iterator of random numbers (between 0 and 1).

### Args

- min (float, optional): random minimum value. Defaults to 0.
- max (float, optional): random maximum value. Defaults to 1.
- iterations (int | None, optional): number of iterations. If not specified, the iterator is infinite. Defaults to None.

### Raises

- ValueError: if `min` is not between 0 and 1.
- ValueError: if `max` is not between 0 and 1.

## Examples

We want to print 5 random numbers between 0 and 1:

```py
>>> for n in GIter.random(iterations=5):
...     print(n)
0.4284862193489152
0.5138492208477652
0.1642186216596907
0.7071756985540777
0.1989296867558108
```

Actually, we need them to be between `0.3` and `0.7`:

```py
>>> for n in GIter.random(0.3, 0.7, iterations=5):
...     print(n)
0.622657614373154
0.5978495719730659
0.5797190835920357
0.3798532899828557
0.37164734974931724
```
