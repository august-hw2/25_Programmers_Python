def solution(n):
    res = 1 if n%7 else 0
    return n//7 + res

print(solution(n=1))