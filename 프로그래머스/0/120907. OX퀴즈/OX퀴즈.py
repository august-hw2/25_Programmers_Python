def solution(quiz):

    ans = []

    for i in quiz:
        tmp = i.split(' = ')
        if eval(tmp[0]) == int(tmp[1]):
            ans.append("O")
        else:
            ans.append("X")

    return ans