from math import gcd

def solution(a, b):

    b /= gcd(b, a)

    for i in [2, 5]:
        while not b%i:
            b //= i

    return 1 if b == 1 else 2