def solution(strlist):
    res = []
    for i in strlist:
        res.append(len(i))

    return res

print(solution(["We", "are", "the", "world!"]))