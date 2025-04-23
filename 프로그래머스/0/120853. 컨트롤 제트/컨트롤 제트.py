def solution(s):
    tmp = s.split(' ')
    res = 0
    for i in range(len(tmp)):
        if tmp[i] != 'Z':
            res += int(tmp[i])
        else:
            res -= int(tmp[i-1])

    return res