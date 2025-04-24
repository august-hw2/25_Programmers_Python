def solution(arr, queries):
    res = []
    for s, e, k in queries:
        m = [i for i in arr[s:e+1] if i>k]
        res.append(min(m) if m else -1)

    return res