def solution(sides):
    m = max(sides)
    sides.remove(m)

    return 1 if m < sum(sides) else 2

print(solution([1, 2, 3]))