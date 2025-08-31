def solution(s, skip, index):
    answer = []

    ch = [chr(c) for c in range(97, 123) if chr(c) not in skip]

    for i in s:
        answer.append(ch[(ch.index(i)+index)%len(ch)])

    return ''.join(answer)