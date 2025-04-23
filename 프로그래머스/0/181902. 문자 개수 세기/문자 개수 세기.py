def solution(my_string):
    res = [0]*52

    for i in my_string:
        if 65 <= ord(i) <= 90:
            res[ord(i)-65] += 1
        else:
            res[ord(i)-71] += 1

    return res