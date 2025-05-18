def solution(common):
    
    a, b, c = common[:3]
    
    if c-b != b-a: #등비수열
        return common[-1] * (b//a)
    else: #등차수열
        return common[-1] + (b-a)