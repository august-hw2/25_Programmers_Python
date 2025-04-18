def solution(myString):
    res = []

    for i in myString:
        if i < 'l':
            res.append('l')
        else:
            res.append(i)

    return ''.join(res)