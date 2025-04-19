#공차수열 일반항
# an = a1 + (n-1)d
def solution(a, d, included):
    res = 0
    for i in range(len(included)):
        if included[i] == True:
            res += a+i*d
    return res