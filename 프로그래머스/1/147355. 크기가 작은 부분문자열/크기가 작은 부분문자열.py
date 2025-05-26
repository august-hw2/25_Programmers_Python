def solution(t, p):
    answer = 0

    for i in range(len(t)):
        tmp = t[i:i+len(p)]
        if len(tmp) == len(p) and int(tmp) <= int(p):
            answer += 1

    return answer