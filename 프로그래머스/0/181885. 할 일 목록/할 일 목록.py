def solution(todo_list, finished):

    res = []

    for i in range(len(finished)):
        if finished[i] == False:
            res.append(todo_list[i])

    return res