def solution(myString, pat):
    myString = myString.lower()
    myString = myString.replace('b', 'A')
    myString = myString.replace('a', 'B')
    return 1 if pat in myString else 0
