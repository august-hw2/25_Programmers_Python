def solution(arr, k):
    tmp = []
    seen = set()

    for i in arr:
        if i not in seen:
            seen.add(i)
            tmp.append(i)
        if len(tmp) == k:
            break

    return tmp + [-1] * (k-len(tmp))