# FrogRiverOne


def solution(X, A):
    leaves = set()
    for i, j in enumerate(A):
        if j <= X:
            leaves.add(j)
        if len(leaves) == X: return i
    return -1


if __name__ == "__main__":
    print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))



