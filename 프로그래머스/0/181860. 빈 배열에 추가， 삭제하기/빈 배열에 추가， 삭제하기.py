def solution(arr, flag):
    res = []

    for i, j in zip(arr, flag):
        if j == True:
            res += [i]*(i*2)
        else:
            res = res[:-i]

    return res