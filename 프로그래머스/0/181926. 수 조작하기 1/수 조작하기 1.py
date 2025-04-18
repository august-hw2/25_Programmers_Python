def solution(n, control):

    key = dict(zip(['w','s','d','a'], [1, -1, 10, -10]))

    for i in control:
        n += key.get(i)

    return n