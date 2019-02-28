# OddOccurrencesInArray
def solution(A):
    start_number = 0
    for num in A :
        start_number = num ^ start_number
    return start_number


# another solution

