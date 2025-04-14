def solution(arr):
    res = []

    for i in arr:
        res.extend([i]*i)

    return res