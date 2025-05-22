def solution(polynomial):

    x, num = 0, 0
    for i in polynomial.split(' + '):
        if 'x' == i:
            x += 1
        elif 'x' in i:
            x += int(i.replace('x',''))
        else:
            num += int(i)

    if x and num:
        return f"{x}x + {num}" if x>1 else f"x + {num}"
    elif x:
        return f"{x}x" if x>1 else f"x"
    else:
        return str(num)