def solution(num_list):
    return [sum(1 for i in num_list if i%2==0), sum(1 for i in num_list if i%2!=0)]

print(solution(num_list=[1, 2, 3, 4, 5]))