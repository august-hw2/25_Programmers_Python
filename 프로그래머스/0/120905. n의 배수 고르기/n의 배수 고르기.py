def solution(n, numlist):
    res = []

    for i in numlist:
        if i%n == 0:
            res.append(i)

    return res


print(solution(n = 3, numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]))