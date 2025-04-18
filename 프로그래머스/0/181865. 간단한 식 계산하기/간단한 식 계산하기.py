def solution(binomial):
    res = binomial.split(' ')
    a, b = int(res[0]), int(res[2])
    if res[1] == '+':
        return a+b
    elif res[1] == '-':
        return a-b
    elif res[1] == '*':
        return a*b