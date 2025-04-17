def solution(n):
    res = [n]
    while True:
        if n == 1:
            break
        if n%2: #홀수일 때
            n = 3*n+1
        else: #짝수일 때
            n //= 2
        res.append(n)
    return res