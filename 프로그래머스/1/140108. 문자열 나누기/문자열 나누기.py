def solution(s):
    answer = 0
    # 기준 문자 (+1), 다른 문자 (-1)
    bal = 0
    base = None # 현재 구간의 기준 문자

    for ch in s:
        if bal == 0:
            base = ch
        bal += 1 if ch == base else -1
        
        if bal == 0:
            answer += 1
            
    # 끝났는데, 균형 안 맞으면 마지막 구간 1개 추가        
    if bal != 0:
        answer += 1

    return answer