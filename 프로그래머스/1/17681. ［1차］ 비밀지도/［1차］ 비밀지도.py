def solution(n, arr1, arr2):
    answer = []

    for a1, a2 in zip(arr1, arr2):
        a_1, a_2 = bin(a1)[2:].zfill(n), bin(a2)[2:].zfill(n)
        tmp = []
        for i, j in zip(a_1, a_2):
            if int(i)|int(j):
                tmp.append('#')
            else:
                tmp.append(' ')
        answer.append(''.join(tmp))

    return answer