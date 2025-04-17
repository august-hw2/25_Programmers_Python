def solution(my_strings, parts):
    res = []
    for m, p in zip(my_strings, parts):
        i, j = p
        res.append(m[i:j+1])
    return ''.join(res)