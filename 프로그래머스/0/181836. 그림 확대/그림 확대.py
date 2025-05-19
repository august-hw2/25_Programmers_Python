def solution(picture, k):
    answer = []

    for i in picture:
        tmp = []
        for j in i:
            tmp.append(j*k)
        for p in range(k):
            answer.append(''.join(tmp))

    return answer