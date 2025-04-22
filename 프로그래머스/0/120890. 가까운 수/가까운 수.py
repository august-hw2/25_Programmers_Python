def solution(array, n):
    array.sort()
    tmp = []
    for i in array:
        tmp.append(abs(n-i))

    return array[tmp.index(min(tmp))]