"""
This file exists to try some stuff from the library.
If Pyglit becomes an actual thing, it is most likely not to stay.
"""

from pyglit import GIter


def main() -> None:
    for n in GIter.syracuse(15):
        print(n, end=" ")


if __name__ == "__main__":
    main()
