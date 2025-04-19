def solution(intStrs, k, s, l):
    res = []
    for i in intStrs:
        if int(i[s:s+l]) > k:
            res.append(int(i[s:s+l]))
    return res