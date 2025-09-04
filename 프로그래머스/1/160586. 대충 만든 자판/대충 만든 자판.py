def solution(keymap, targets):
    alpha = {}
    
    # 최소 입력 횟수 사전 만들기
    for k in keymap:
        for idx, ch in enumerate(k, start=1): # 1부터 인덱스 값 시작
            if ch in alpha: # 더 작은 인덱스만 저장
                alpha[ch] = min(alpha[ch], idx)
            else:
                alpha[ch] = idx

    answer = []

    for t in targets:
        s = 0  # 각 문자열에 맞는 최소 위치 합
        for i in t:
            v = alpha.get(i)
            if v is None:   # 없으면 None, 해당 문자를 만들 수 없음
                s = -1
                break
            s += v
        answer.append(s)

    return answer