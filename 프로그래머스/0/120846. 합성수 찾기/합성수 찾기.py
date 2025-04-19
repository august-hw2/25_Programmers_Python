def solution(n):
    res = 0
    for i in range(4, n+1): #합성수는 4부터 해당됨
        for j in range(2, int(i**0.5)+1): #제곱근으로 약수 개수 구함
            if i%j == 0:
                res += 1
                break
    return res