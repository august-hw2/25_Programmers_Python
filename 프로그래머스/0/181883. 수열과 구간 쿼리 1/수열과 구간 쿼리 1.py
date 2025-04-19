def solution(arr, queries):

    for n in queries:
        i, j = n
        for m in range(i, j+1):
            arr[m] += 1

    return arr