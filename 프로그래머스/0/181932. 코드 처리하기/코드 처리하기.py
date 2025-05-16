def solution(code):
    answer = ''
    mode = 0

    for i, char in enumerate(code):
        if mode == 0:
            if char != '1' and i%2 == 0:
                answer += char
            elif char == '1':
                mode = 1
        elif mode == 1:
            if char != '1' and i%2:
                answer += char
            elif char == '1':
                mode = 0
    return answer if len(answer) else "EMPTY"