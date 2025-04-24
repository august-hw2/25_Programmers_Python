def solution(my_string, queries):
    res = list(my_string)

    for i, j in queries:
        res[i:j+1] = res[i:j+1][::-1]

    return ''.join(res)