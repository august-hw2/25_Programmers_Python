def solution(num):
    cnt = 0
    
    if num == 1:
        return cnt
    
    while True:

        if num%2 == 0: #짝수
            num //= 2
        else: #홀수
            num = num*3 + 1
    
        cnt += 1

        if num == 1:
            return cnt

        if cnt == 500:
            return -1