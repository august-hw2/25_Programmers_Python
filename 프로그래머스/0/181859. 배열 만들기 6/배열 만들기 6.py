def solution(arr):
    stk = []
    for i in arr:
        if stk and stk[-1] == i:
            stk.pop(-1)
        else:
            stk.append(i)

    return stk if stk else [-1]