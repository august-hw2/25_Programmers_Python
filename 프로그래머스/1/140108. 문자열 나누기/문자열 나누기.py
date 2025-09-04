def solution(s):
    answer = 0
    # 기준 문자 개수, 다른 문자 개수
    x = y = 0

    for ch in s:
        if x == 0:
            tmp = ch
            x += 1
        else:
            if tmp == ch:
                x += 1
            else:
                y += 1

        if x == y:
            answer += 1
            x = y = 0
            
    if x != y:
        answer += 1

    return answer