def solution(s):
    answer = []
    tmp = []

    for i in s:
        if i not in tmp:
            tmp.append(i)
            answer.append(-1)
        else:
            answer.append(len(tmp) - ''.join(tmp).rfind(i))
            tmp.append(i)

    return answer