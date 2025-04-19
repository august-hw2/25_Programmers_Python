def solution(num_list):
    cnt = 0
    for i in num_list:
        tmp = i
        while tmp != 1:
            tmp = (tmp-1)//2 if tmp%2 else tmp//2
            cnt += 1
    return cnt