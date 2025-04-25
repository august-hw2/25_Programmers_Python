def solution(sides):
    res = 0
    m = max(sides)
    n = min(sides)

    # sides에 있는 변(max_sides)이 가장 길 경우
    for new_side in range(m - n + 1, m + 1):
        res += 1

    # 새로운 변(new_side)가 가장 길 경우
    for new_side in range(m + 1, m + n):
        res += 1

    return res