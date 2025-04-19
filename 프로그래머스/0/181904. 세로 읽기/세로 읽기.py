def solution(my_string, m, c):
    res=[]
    for i in range(0, len(my_string), m):
        res.append(my_string[i:i+m][c-1])
    return ''.join(res)