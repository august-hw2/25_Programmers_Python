def solution(i, j, k):
    res = 0

    for n in range(i, j+1):
        if str(k) in str(n):
            res += str(n).count(str(k))

    return res