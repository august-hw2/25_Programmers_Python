def solution(a, b):
    return max(int(str(a)+str(b)), int(str(b)+str(a)))
    #return int(str(a)+str(b)) if int(str(a)+str(b)) > int(str(b)+str(a)) else int(str(b)+str(a))