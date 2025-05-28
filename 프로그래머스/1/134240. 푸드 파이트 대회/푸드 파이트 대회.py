def solution(food):
    answer = []
    cnt = [i//2 for i in food]

    for j in range(len(cnt)):
        answer.append(str(j)*cnt[j])

    return ''.join(answer[1:]) + '0' + ''.join(answer[1:])[::-1]
