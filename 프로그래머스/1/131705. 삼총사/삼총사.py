from itertools import combinations
#조합: 뽑은 순서 고려 x

def solution(number):
    answer = 0

    for i in combinations(number, 3):
        if sum(i) == 0:
            answer += 1

    return answer