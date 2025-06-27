from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    cnt = Counter(dice)

    if len(cnt) == 1:
        return a * 1111
    elif len(cnt) == 2:
        for num in cnt:
            if cnt[num] == 3:
                p = num
                q = [x for x in cnt if x != p][0]
                return (10 * p + q) ** 2  # ← 수정된 부분
        p, q = cnt.keys()
        return (p + q) * abs(p - q)
    elif len(cnt) == 3:
        ones = [num for num, count in cnt.items() if count == 1]
        return ones[0] * ones[1]
    else:
        return min(dice)