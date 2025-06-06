def count(num):

    cnt = 0

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            cnt += 1
            if i ** 2 != num:
                cnt += 1

    return cnt

def solution(number, limit, power):
    answer = []

    for i in range(1, number+1):
        c = count(i)
        answer.append(c if c <= limit else power)

    return sum(answer)