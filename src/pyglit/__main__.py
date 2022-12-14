"""
This file exists to try some stuff from the library.
If Pyglit becomes an actual thing, it is most likely not to stay.
"""

from pyglit import GIter


def main() -> None:
    for n in GIter.syracuse(5):
        print(n)


if __name__ == "__main__":
    main()
