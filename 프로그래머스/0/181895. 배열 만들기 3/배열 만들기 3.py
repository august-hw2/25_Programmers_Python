def solution(arr, intervals):
    res = []
    for n in intervals:
        i, j = n
        res.extend(arr[i:j+1])
    return res