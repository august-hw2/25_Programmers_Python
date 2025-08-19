
def solution(survey, choices):
    answer = []

    case = { # 유형별 점수표
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0,
    }

    point = { # 매우 비동의 ~ 매우 동의
        1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3
    }

    for s, c in zip(survey, choices):
        one, two = s[0], s[1]
        if c in (1, 2, 3):
            case[one] += point[c]
        elif c in (5, 6, 7):
            case[two] += point[c]

    # 각 지표를 쌍으로 구성한 뒤, 큰 값인 문자 더하기
    pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]

    for a, b in pairs:
        if case[a] > case[b]:
            answer.append(a)
        elif case[a] < case[b]:
            answer.append(b)
        else:
            answer.append(min(a, b))

    return ''.join(answer)