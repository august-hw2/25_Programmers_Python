def solution(food):
    answer = ''

    for j in range(1, len(food)):
        answer += str(j)*(food[j]//2)

    return answer + '0' + answer[::-1]