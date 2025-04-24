def solution(arr):
    stk = []
    for i in arr:
        while stk and stk[-1] >= i:
            stk.pop()
        else:
            stk.append(i)
    return stk