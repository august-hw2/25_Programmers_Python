def solution(chicken):

    ans = 0

    while chicken >= 10:
        div = chicken // 10
        mod = chicken % 10
        ans += div
        chicken = div + mod

    return ans