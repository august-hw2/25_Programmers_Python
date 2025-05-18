import math

def solution(numer1, denom1, numer2, denom2):
    l = denom1 * denom2 // math.gcd(denom1, denom2)

    n3 = numer1 * (l//denom1) + numer2 * (l//denom2)
    d3 = l

    return [n3 // math.gcd(n3, d3), d3 // math.gcd(n3, d3)]