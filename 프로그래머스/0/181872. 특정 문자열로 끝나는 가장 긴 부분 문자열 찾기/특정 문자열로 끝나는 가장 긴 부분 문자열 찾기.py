def solution(myString, pat):

    for i in range(len(myString[::-1])):
        if myString[::-1][i:i+len(pat[::-1])] == pat[::-1]:
            return myString[::-1][i:][::-1]