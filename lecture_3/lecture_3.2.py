def solution(A):
    if len(A) == 1:
        return A[0]
    if len(A) == 0:
        return 0
    bottom = sorted(A)[-1]
    up = sorted(A)[0]
    total = ((up + bottom) * ( bottom - up + 1)) // 2
    if total - sum(A) != 0:
        return total - sum(A)


if __name__ == "__main__":
    print(solution([2, 3, 1, 5]))
