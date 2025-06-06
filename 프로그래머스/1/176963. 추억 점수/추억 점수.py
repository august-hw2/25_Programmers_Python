def solution(name, yearning, photo):
    answer = []
    info = dict(zip(name, yearning))

    for i in photo:
        score = 0
        for j in i:
            score += info.get(j, 0)

        answer.append(score)

    return answer