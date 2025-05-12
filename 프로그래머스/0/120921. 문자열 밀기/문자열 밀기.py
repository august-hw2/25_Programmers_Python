def solution(A, B):
    
    if len(A) != len(B):
        return -1
    
    double_B = B * 2
    
    return double_B.find(A) if A in double_B else -1