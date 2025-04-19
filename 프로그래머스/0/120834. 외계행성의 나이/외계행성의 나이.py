def solution(age):
    s = str(age)
    res = []
    for i in s:
        res.append(chr(ord('a')+int(i)))
    return ''.join(res)