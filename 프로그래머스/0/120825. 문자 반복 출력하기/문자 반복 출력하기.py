def solution(my_string, n):
    return ''.join([i*n for i in my_string])

print(solution(my_string="hello", n=3))