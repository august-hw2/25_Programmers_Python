def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    answer = 0

    for b in babbling:
        for c in can:
            if c in b: #입력 예시에 할 수 있는 단어가 있는지 확인
                b = b.replace(c, '*') #있으면 간단하게 대체
        if len(b) == b.count('*'): #별 개수와 단어 길이가 동일하면 할 수 있는 말로 판정
            answer += 1

    return answer