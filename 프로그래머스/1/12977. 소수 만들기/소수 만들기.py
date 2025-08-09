import math
from itertools import combinations

def solution(nums):
    check = list(combinations(nums, 3))

    answer = len(check)

    for i in check:
        tmp = sum(i)
        for j in range(2, int(math.sqrt(tmp)) + 1):
            # x가 해당 수로 나누어떨어진다면
            if tmp % j == 0: # 소수가 아니므로, 전체 숫자 수에서 1개씩 빼기
                answer -= 1
                break

    return answer