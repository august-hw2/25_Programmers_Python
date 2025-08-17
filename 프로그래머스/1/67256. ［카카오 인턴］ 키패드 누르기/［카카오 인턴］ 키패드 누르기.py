def distance(h, p, l, r):

    (x1, y1) = p
    (x2, y2) = l
    (x3, y3) = r

    l_p = abs(x2-x1) + abs(y2-y1)
    r_p = abs(x3-x1) + abs(y3-y1)

    if l_p < r_p:
        return 'L'
    elif l_p > r_p:
        return 'R'
    else:
        return 'L' if h == 'left' else 'R'

def solution(numbers, hand):
    answer = ''
    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]

    # numbers에 있는 숫자 위치를 모두 딕셔너리로 미리 만들기
    pos = {}
    for r, row in enumerate(keypad): # r은 인덱스, row는 값 -> keypad[0] = ['1', '2', '3']
        for c, val in enumerate(row): # c은 인덱스, row는 값 -> row[0] = ['1']
            pos[val] = [r, c]
            
    # 시작 위치 초기화
    left = pos['*']
    right = pos['#']

    for i in numbers:
        point = pos[str(i)]
        if i in (1, 4, 7):
            answer += 'L'
            left = point
        elif i in (3, 6, 9):
            answer += 'R'
            right = point
        else:
            # 왼손과 오른손의 각각 거리 계산
            choose = distance(hand, point, left, right)
            answer += choose
            
            # 선택한 손의 위치 갱신
            if choose == 'L':
                left = point
            else:
                right = point

    return answer