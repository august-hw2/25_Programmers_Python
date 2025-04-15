def solution(arr):
    res = []
    for i in arr:
        if i >= 50 and i%2 == 0:
            res.append(i//2)
        elif i < 50 and i%2 != 0:
            res.append(i*2)
        else:
            res.append(i)

    return res