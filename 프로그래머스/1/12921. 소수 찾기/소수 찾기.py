def is_prime(num):

    for j in range(2, int(num ** 0.5) + 1):
        if num%j == 0:
            return False
    return True

def solution(n):
    answer = 0

    for i in range(2, n+1):
        if is_prime(i):
            answer += 1

    return answer
