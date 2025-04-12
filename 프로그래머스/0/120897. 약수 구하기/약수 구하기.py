def solution(n):
    res = []
    for i in range(1, int(n**0.5)+1):
        #제곱근으로 구해서, 시간 감소
        if n%i == 0:
            res.append(i)
            if (i**2) != n:
                #i가 제곱근인 경우 제외해주는 조건문
                res.append(n//i)
    return sorted(res)