def solution(my_string):
    res = ''
    for i in my_string:
        if i.islower():
            res += i.upper()
        else:
            res += i.lower()

    return res