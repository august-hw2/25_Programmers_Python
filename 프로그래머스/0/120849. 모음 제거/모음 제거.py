def solution(my_string):
    res = ""
    for i in my_string:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            res += i

    return res

print(solution("bus"))