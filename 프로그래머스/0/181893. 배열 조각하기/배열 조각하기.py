def solution(arr, query):
    answer = arr

    for idx, num in enumerate(query):
        if idx%2: #홀수
            del answer [:num]
        else: #짝수
            del answer [num+1:]

    return answer