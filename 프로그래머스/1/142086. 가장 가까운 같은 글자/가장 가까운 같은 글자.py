def solution(s):
    last_index = dict()
    result = []

    for idx, char in enumerate(s):
        if char in last_index:
            result.append(idx - last_index[char])
        else:
            result.append(-1)
        last_index[char] = idx

    return result