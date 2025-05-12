from collections import deque

def solution(A, B):
    dq = deque(B)

    if A == B:
        return 0

    for i in range(len(A)):
        dq.rotate(-1)
        if ''.join(list(dq)) == A:
            return i+1

    return -1