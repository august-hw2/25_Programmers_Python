def solution(s):
    stack = []
    for i in s.split():
        if i != 'Z':
            stack.append(int(i))
        else:
            if stack:
                stack.pop()
    return sum(stack)