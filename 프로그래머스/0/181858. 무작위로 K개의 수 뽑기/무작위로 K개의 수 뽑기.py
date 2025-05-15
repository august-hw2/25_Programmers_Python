def solution(arr, k):
    tmp = []
    
    for i in arr:
        if i not in tmp:
            tmp.append(i)
        if len(tmp) == k:
            break
    
    return tmp + [-1] * (k-len(tmp))