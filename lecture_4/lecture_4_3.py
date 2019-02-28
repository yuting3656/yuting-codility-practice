# MissingInteger


def solution(A):
    A.sort()
    min_num = 1
    for i in A:
        if i > min_num:
            return min_num
        if i > 0:
            min_num = i + 1

    return min_num


if __name__ == "__main__":
    pass
