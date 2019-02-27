def solution(A):
    return 1 if len(A) == 0 else int((max(A) * (max(A) +1) * 0.5) - sum(A))

if __name__ == "__main__":
    print(solution([2, 3, 1, 5]))
