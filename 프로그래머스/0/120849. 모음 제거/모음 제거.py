def solution(my_string):
    res = ""
    for i in my_string:
        if i not in "aeiou": #문자열이 리스트이기 때문에 가능.
            res += i

    return res

print(solution("bus"))