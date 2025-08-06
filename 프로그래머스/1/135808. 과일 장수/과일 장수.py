def solution(k, m, score):
    answer = 0

    score.sort(reverse=True)
    slice_score = score[:len(score)-(len(score)%m)]

    for i in range(m-1, len(slice_score), m):
        answer = answer + (score[i]*m)

    return answer