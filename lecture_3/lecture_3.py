""""
X+Dx > Y
10+ 30x > 85
"""


def solution(X, Y, D):
    global num
    num = 0
    if X >= Y:
        return 0
    new_x = X
    while not (new_x > Y):
        new_x = X + D
        num += 1
        if new_x > Y:
            return num


def solution2(X, Y, D):
    global x
    x = 1
    while 1:
        x += 1
        if D*x + X >= Y:
            return x


def solution3(X, Y, D):
    if (Y - X) % D == 0:
        return (Y - X) // D
    else:
        return (Y - X) // D + 1


if __name__ == "__main__":
    solution(10, 85, 30)