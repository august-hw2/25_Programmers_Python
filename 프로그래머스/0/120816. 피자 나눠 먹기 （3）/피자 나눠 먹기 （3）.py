def solution(slice, n):
    res = 1 if n%slice else 0
    return n//slice + res

print(solution(slice=7, n=10))