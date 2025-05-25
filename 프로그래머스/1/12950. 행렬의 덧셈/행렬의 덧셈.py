def solution(arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        answer.append([i[k]+j[k] for k in range(len(i))])

    return answer