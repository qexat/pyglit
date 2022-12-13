from pyglit import GIter


def main() -> None:
    l = [3, 5, 2, 1]
    giter = GIter.from_choice(l, consume=False, max_size=10)
    for i in giter:
        print(i)


if __name__ == "__main__":
    main()
