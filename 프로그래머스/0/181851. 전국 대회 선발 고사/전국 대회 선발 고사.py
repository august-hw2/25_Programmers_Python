def solution(rank, attendance):
    tmp = []

    for r, a in zip(rank, attendance):
        if a:
            tmp.append(r)

    tmp.sort()

    return 10000*rank.index(tmp[0]) + 100*rank.index(tmp[1]) + rank.index(tmp[2])