import collections


def solutions(a, k):
    if len(a) == 0:
        return a
    col_de = collections.deque(a)
    col_de.rotate(k % len(a))
    return list(col_de)


if __name__ == "__main__":
    solutions([1, 2, 3, 4], 2)
