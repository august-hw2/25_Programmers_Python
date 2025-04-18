def solution(arr, delete_list):
    res = []
    for i in arr:
        if i not in delete_list:
            res.append(i)
    return res