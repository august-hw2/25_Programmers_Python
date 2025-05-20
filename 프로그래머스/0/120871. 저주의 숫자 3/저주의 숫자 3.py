def solution(n):

    answer = []
    i = 1

    while len(answer) < n:

        if '3' in str(i) or i%3 == 0:
            pass
        else:
            answer.append(i)
        i += 1

    return answer[-1]