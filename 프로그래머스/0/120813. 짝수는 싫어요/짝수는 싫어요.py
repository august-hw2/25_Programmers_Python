def solution(n):
    return [i for i in range(1, n+1, 2)]
    #return [x for x in range(n + 1) if x % 2]

print(solution(n=10))