def solution(numbers, direction):
    if direction == 'right':
        tmp = numbers.pop(-1)
        numbers.insert(0, tmp)
    else:
        tmp = numbers.pop(0)
        numbers.append(tmp)

    return numbers