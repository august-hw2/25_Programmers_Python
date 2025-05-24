from math import sqrt

def solution(n):

    if int(sqrt(n))**2 == n:
        return (int(sqrt(n))+1)**2
    else:
        return -1