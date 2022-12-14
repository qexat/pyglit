from __future__ import annotations

from collections.abc import Callable
from collections.abc import Generator
from collections.abc import Iterator
from collections.abc import Sequence
from random import randint
from random import random
from typing import Any
from typing import Generic
from typing import overload
from typing import TypeVar

from bepospliz import anon_args

T_co = TypeVar("T_co", covariant=True)
R = TypeVar("R")

__all__ = ("GIter",)


class GIter(Generic[T_co]):
    @classmethod
    @overload
    def range(cls, stop: int, /) -> GIter[int]:
        ...

    @classmethod
    @overload
    def range(cls, start: int, stop: int, /) -> GIter[int]:
        ...

    @classmethod
    @overload
    def range(cls, start: int, stop: int, step: int, /) -> GIter[int]:
        ...

    @classmethod
    def range(
        cls,
        start: int,
        stop: int | None = None,
        step: int = 1,
        /,
    ) -> GIter[int]:
        """
        Create an iterator given start*, stop and step* values. (*: optional)

        Args:
            start (int): start value of range (inclusive). Defaults to 0.
            stop (int | None, optional): stop value of range (exclusive).
            step (int, optional): step value of range. Defaults to 1, cannot be 0.

        Raises:
            ValueError: if step equals 0.

        This method exists for completeness ; you probably want to use Python's built-in `range` instead.
        """

        if not step:
            raise ValueError("step cannot be zero")

        i_start = 0 if stop is None else start
        i_stop = start if stop is None else stop
        i_step = step

        def generator() -> Generator[int, None, None]:
            begin, end, step = i_start, i_stop, i_step
            i = begin
            while begin <= (i + step) and i < end:
                yield i
                i += step

        return GIter(generator())

    @classmethod
    @overload
    def random(
        cls,
        *,
        iterations: int | None = None,
    ) -> GIter[float]:
        ...

    @classmethod
    @overload
    def random(
        cls,
        min: float = 0,
        max: float = 1,
        *,
        iterations: int | None = None,
    ) -> GIter[float]:
        ...

    @classmethod
    def random(
        cls,
        min: float = 0,
        max: float = 1,
        *,
        iterations: int | None = None,
    ) -> GIter[float]:
        """
        Create an iterator of random numbers (between 0 and 1).

        Args:
            min (float, optional): random minimum value. Defaults to 0.
            max (float, optional): random maximum value. Defaults to 1.
            iterations (int | None, optional): number of iterations. If not specified, the iterator is infinite. Defaults to None.

        Raises:
            ValueError: if `min` is not between 0 and 1.
            ValueError: if `max` is not between 0 and 1.
        """

        if min < 0 or min > 1:
            raise ValueError("min must be between 0 and 1")
        if max < 0 or max > 1:
            raise ValueError("max must be between 0 and 1")

        if iterations is not None and iterations < 0:
            raise ValueError("iterations cannot be negative")

        def generator() -> Generator[float, None, None]:
            _min, _max, i, i_max = (
                min,
                max,
                0,
                1 if iterations is None else iterations,
            )
            while i < i_max:
                if _min <= (r := random()) < _max:
                    # if infinite, increment i_max so i is never above
                    if iterations is None:
                        i_max += 1
                    i += 1

                    yield r

        return GIter(generator())

    @classmethod
    def randint(
        cls,
        int_min: int,
        int_max: int,
        *,
        iterations: int | None = None,
    ) -> GIter[int]:
        """
        Create an iterator of random integers.

        Args:
            int_min (int): the minimum integer value (`randint`'s `a`).
            int_max (int): the maximum integer value (`randint`'s `b`).
            iterations (int | None, optional): number of iterations. If not specified, the iterator is infinite. Defaults to None.

        Raises:
            ValueError: if `int_min` is bigger than `int_max`.
        """

        if int_min > int_max:
            raise ValueError("min must be smaller than max")

        if iterations is not None and iterations < 0:
            raise ValueError("iterations cannot be negative")

        def generator() -> Generator[int, None, None]:
            i, i_max = 0, 1 if iterations is None else iterations
            while i < i_max:
                # if infinite, increment i_max so i is never above
                if iterations is None:
                    i_max += 1

                i += 1
                yield randint(int_min, int_max)

        return GIter(generator())

    @classmethod
    def choice(
        cls,
        seq: Sequence[T_co],
        *,
        consume: bool = True,
        max_size: int | None = None,
    ) -> GIter[T_co]:
        """
        Create an iterator from a sequence that yields randomly an element.
        By default, consumes this latter ; this can be set off, which would make the iterator infinite except if you set a maximum size.

        Args:
            seq (Sequence[T]): the sequence used to build the iterator.
            consume (bool, optional): if the picked elements are popped off the iterator. Defaults to True.
            max_size (int, optional): sets the iterator max size (useful if `consume` is set to False). Defaults to None.

        Example:
        >>> l = [3, 5, 2, 1]
        >>> g = GIter.from_choice(l, consume=False, max_size=10)
        >>> for i in g:
        ...     print(i, end=" ")
        1 2 1 1 2 2 3 5 3 2

        Remember when you learned probability in high school using bags filled with balls? That's basically that :D
        """

        if max_size is not None and max_size < 0:
            raise ValueError("max size cannot be negative")

        def generator() -> Generator[T_co, None, None]:
            temp_list = list(seq)
            c = -1 if max_size is None else max_size

            # It is not c < 0 because we want the iterator to be infinite
            # if `max_size` is not set and `consume` is set to False
            while temp_list and c != 0:
                seq_len = len(temp_list)
                index = randint(0, seq_len - 1)
                yield temp_list[index]

                if consume:
                    temp_list.pop(index)

                c -= 1

        return GIter(generator())

    @classmethod
    def syracuse(cls, starting: int, *, include_starting: bool = False) -> GIter[int]:
        """
        Create an iterator of all the integers that follow `starting` in the Syracuse sequence according to the Collatz conjecture.

        See: <https://en.wikipedia.org/wiki/Collatz_conjecture>

        Args:
            starting (int): the integer to start from.
            include_starting (bool, optional): whether the starting integer should be included. Defaults to False.

        Raises:
            ValueError: if the starting integer is not positive.
        """

        if starting <= 0:
            raise ValueError("starting integer must be strictly positive")

        def generator() -> Generator[int, None, None]:
            value: int = starting

            if include_starting:
                yield value

            while value != 1:
                value = value // 2 if value % 2 == 0 else 3 * value + 1
                yield value

        return GIter(generator())

    @overload
    @anon_args
    def __init__(
        self,
        generator: Generator[T_co, None, None],
    ) -> None:
        ...

    @overload
    @anon_args
    def __init__(
        self,
        generator: Generator[T_co, None, None],
        function: Callable[[T_co], Any] | None,
    ) -> None:
        ...

    @anon_args
    def __init__(
        self,
        generator: Generator[T_co, None, None],
        function: Callable[[T_co], Any] | None = None,
    ) -> None:
        self.__generator = generator
        self.__function: Callable[[T_co], Any] | None = function

    def __iter__(self) -> Iterator[T_co]:
        return self.__generator

    # *-- WIP: NOT DOCUMENTED FOR NOW --* #

    def map(self, function: Callable[[T_co], Any]) -> GIter[T_co]:
        self.__function = function
        return self

    def run(self) -> None:
        for i in self.__generator:
            if self.__function:
                self.__function(i)
