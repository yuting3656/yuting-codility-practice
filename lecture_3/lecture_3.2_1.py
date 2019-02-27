def solution(A):
    print(sum(range(1, len(A)+2)))
    print(sum([a for a in A]))
    return sum(range(1, len(A)+2))-sum([a for a in A])


if __name__ == "__main__":
    print(solution([2, 3, 1, 5]))
