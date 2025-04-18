def solution(numLog):
    res = []
    for i in range(len(numLog)-1):
        tmp = numLog[i+1] - numLog[i]
        if tmp == 1:
            res.append('w')
        elif tmp == -1:
            res.append('s')
        elif tmp == 10:
            res.append('d')
        elif tmp == -10:
            res.append('a')

    return ''.join(res)