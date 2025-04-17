def solution(my_string, index_list):
    res = []

    for i in index_list:
        res.append(my_string[i])

    return ''.join(res)