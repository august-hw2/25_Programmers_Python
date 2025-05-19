def solution(picture, k):
    answer = []

    for row in picture:
        tmp = ''.join(p * k for p in row)
        answer.extend([tmp]*k)

    return answer