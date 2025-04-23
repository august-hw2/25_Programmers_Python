def solution(q, r, code):

    return ''.join([code[i] for i in range(len(code)) if r == i%q])