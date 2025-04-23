def solution(order):
    res = 0
    for i in order:
        if "cafe" in i:
            res += 5000
        elif "ameri" in i:
            res += 4500
        else:
            res += 4500
    return res