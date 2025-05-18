def solution(common):
    answer = 0

    if common[2]-common[1] != common[1]-common[0]: #등비수열
        return common[0] * (common[1]//common[0])**(len(common))
    else: #등차수열
        return common[0] + len(common) * (common[1]-common[0])

'''
> 등차수열
An = a + (n - 1) * d

> 등비수열
An = a * r^(n - 1)
'''