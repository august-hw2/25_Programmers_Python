def solution(lottos, win_nums):
    win_set = set(win_nums)
    zero_cnt = lottos.count(0)
    match = sum(1 for x in lottos if x and x in win_set)

    rank = [6, 6, 5, 4, 3, 2, 1]  # 맞춘 개수 → 등수 매핑
    return [rank[match + zero_cnt], rank[match]]