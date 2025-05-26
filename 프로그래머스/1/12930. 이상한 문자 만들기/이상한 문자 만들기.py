def solution(s):
    answer = []
    arr = s.split(' ')

    for i in arr:
        tmp = []
        for j in range(len(i)):
            if j%2:
                tmp.append(i[j].lower())
            else:
                tmp.append(i[j].upper())
        answer.append(''.join(tmp))

    return ' '.join(answer)