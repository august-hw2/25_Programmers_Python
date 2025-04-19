def solution(arr, flag):
    res = []

    for i in range(len(flag)):
        if flag[i] == True:
            res += [arr[i]]*(arr[i]*2)
        else:
            res = res[:-arr[i]]

    return res