def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        answer[i % 2] += 1 #i%2 == 0 혹은 1이기 때문에 배열의 인덱스는 0 또는 1만 나옴
    return answer

print(solution(num_list=[1, 2, 3, 4, 5]))