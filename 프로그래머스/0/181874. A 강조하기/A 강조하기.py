def solution(myString):
    res = []
    for i in myString:
        if i == 'a':
            res.append(i.upper())
        elif i == 'A':
            res.append(i)
        else:
            res.append(i.lower())

    return ''.join(res)