def solution(num_list):

    if len(num_list) >= 11:
        return sum(num_list)
    else:
        res = 1
        for i in num_list:
            res *= i
        return res