def solution(strArr):
    res = [0] * 31
    for i in strArr:
        res[len(i)] += 1

    return max(res)