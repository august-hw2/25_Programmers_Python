def solution(my_string):
    res = []
    for i in my_string:
        if i not in res:
            res.append(i)

    return ''.join(res)