def solution(n):

    ans, cnt = 0, 0

    while cnt < n:

        ans += 1

        if '3' in str(ans) or ans%3 == 0:
            continue

        cnt += 1

    return ans