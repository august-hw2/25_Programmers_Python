from math import factorial

def solution(n):
    return max(i for i in range(1, 11) if factorial(i) <= n)