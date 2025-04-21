def solution(arr, queries):
    for n in queries:
        i, j = n
        arr[i], arr[j] = arr[j], arr[i]

    return arr