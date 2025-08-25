def solution(babbling):

    possible = ["aya", "ye", "woo", "ma"]

    answer = 0

    for b in babbling:
        for p in possible:
            if p*2 not in b:
                b = b.replace(p, ' ')

        if b.strip() == '':
            answer += 1

    return answer