# 모든 달은 28일까지 있다고 가정
import re

# 년/월/일 -> 일로 바꾸기
def to_days(y, m, d):
    return y*12*28 + m*28 + d

def solution(today, terms, privacies):
    # 년, 월, 일 구분
    ty, tm, td = map(int, today.split('.'))
    today_days = to_days(ty, tm, td) # 오늘의 년, 월, 일 -> 총 일수로 바꾸기

    # 문자열 구분 => 키(약관 종류): 값(유효기간)
    dict_terms = {}
    for t in terms:
        k, v = t.split()
        dict_terms[k] = int(v)

    answer = []

    # 각 개인정보의 만료일 계산 후 비교
    for idx, p in enumerate(privacies, start=1):
        y, m, d, k = re.split(r"[.\s]+", p)
        y, m, d = int(y), int(m), int(d)

        start = to_days(y, m, d)
        end = start + dict_terms[k]*28 - 1 # 만료일 (마지막 유효일)

        if today_days > end:
            answer.append(idx)

    return answer