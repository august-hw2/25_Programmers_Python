def solution(quiz):

    ans = []

    for i in quiz:
        tmp = i.split(' = ')
        x, op, y = tmp[0].split()

        if op == "+":
            j = 'O' if int(x) + int(y) == int(tmp[1]) else 'X'
            ans.append(j)
        else:
            j = 'O' if int(x) - int(y) == int(tmp[1]) else 'X'
            ans.append(j)

    return ans