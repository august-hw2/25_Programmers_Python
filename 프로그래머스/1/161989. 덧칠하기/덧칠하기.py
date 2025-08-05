def solution(n, m, section):
    answer = 0
    idx = 0
    length = len(section)

    while idx < length:
        start = section[idx]
        end = start + m - 1 #start = 0 -> end = 0+4-1 = 3 --> 롤러가 다 칠할 수 있는 영역

        while idx < length and section[idx] <= end:
            idx += 1

        answer += 1

    return answer
