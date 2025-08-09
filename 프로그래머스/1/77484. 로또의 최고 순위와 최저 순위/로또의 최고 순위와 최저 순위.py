def solution(lottos, win_nums):

    zero_cnt = lottos.count(0)
    match = len(set(lottos) & set(win_nums))

    best = min(7 - (match + zero_cnt), 6)
    worst = min(7 - match, 6)

    return [best, worst]