# PermCheck


def solution(A):
    return 1 if set(A) == set(range(1, len(A)+1)) else 0


if __name__ == "__main__":
    solution([4, 1, 3, 2])
