def solution(n, t):
    tmp = 1
    while tmp <= t:
        n *= 2
        tmp += 1

    return n