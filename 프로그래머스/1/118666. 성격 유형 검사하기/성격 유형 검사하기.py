def solution(survey, choices):
    score = {k: 0 for k in "RTCFJMAN"}  # 점수판

    for s, c in zip(survey, choices):
        a, b = s[0], s[1]
        d = c - 4
        if d < 0:
            score[a] += -d
        elif d > 0:
            score[b] += d
        # d == 0이면 아무도 가산점 없음

    pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]

    # 동점이면 쌍에서 앞의 문자를 선택(문제의 사전순 규칙과 동일)
    return ''.join(a if score[a] >= score[b] else b for a, b in pairs)