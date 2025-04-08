def solution(n):
    res = 0

    for i in range(1, int(n**0.5)+1): #n의 제곱근까지만 for문 반복.
        if n%i == 0:
            res += 2 #순서만 다른 경우가 2가지 있기 때문.
            if i*i==n:
                res -= 1 #i가 n의 제곱근이기 때문에, 이건 1가지 경우의 수라서 -1.

    return res

print(solution(n=20))