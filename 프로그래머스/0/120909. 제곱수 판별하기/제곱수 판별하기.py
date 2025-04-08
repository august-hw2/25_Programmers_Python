def solution(n):
    return 1 if int(n**0.5)*int(n**0.5) == n else 2

print(solution(n=144))