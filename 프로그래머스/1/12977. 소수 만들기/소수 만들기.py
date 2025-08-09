import math
from itertools import combinations

def solution(nums):

    answer = 0

    for comb in combinations(nums, 3):

        tmp = sum(comb)

        is_prime = True

        for j in range(2, int(math.sqrt(tmp)) + 1):
            # x가 해당 수로 나누어떨어진다면
            if tmp % j == 0: # 소수가 아니므로, 전체 숫자 수에서 1개씩 빼기
                is_prime = False
                break
        if is_prime:
            answer += 1

    return answer