def solution(num_list):
    even = sum(1 for i in num_list if i%2==0)

    return [even, len(num_list)-even]

print(solution(num_list=[1, 2, 3, 4, 5]))