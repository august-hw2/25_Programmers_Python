def solution(arr):
    res = 0
    old = arr
    while True:
        new = []
        for i in old:
            if i>50 and i%2 == 0:
                i //= 2
            elif i<50 and i%2:
                i = 2*i+1
            new.append(i)
        if new == old:
            break
        else:
            old = new
            res += 1
    return res