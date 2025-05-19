def solution(rank, attendance):

    answer = sorted((r, i) for i, (r, a) in enumerate(zip(rank, attendance)) if a)
    a, b, c = answer[0][1], answer[1][1], answer[2][1]

    return 10000*a + 100*b + c