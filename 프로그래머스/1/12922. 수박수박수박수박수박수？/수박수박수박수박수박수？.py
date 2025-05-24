def solution(n):
    answer = []

    for i in range(n):
        answer.append('박') if i%2 else answer.append('수')

    return ''.join(answer)
