def solution(box, n):
    res = 1
    for i in box:
        res *= i//n
    return res