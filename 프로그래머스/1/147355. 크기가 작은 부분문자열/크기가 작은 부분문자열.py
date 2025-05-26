def solution(t, p):
    p_len = len(p)
    p_int = int(p)
    return sum(int(t[i:i + p_len]) <= p_int for i in range(len(t) - p_len + 1))