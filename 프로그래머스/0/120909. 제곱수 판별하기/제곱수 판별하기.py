def solution(n):
    return 1 if (n**0.5)%1 == 0 else 2 #제곱근이 소수점이 아니면 제곱근 해당

print(solution(n=144))