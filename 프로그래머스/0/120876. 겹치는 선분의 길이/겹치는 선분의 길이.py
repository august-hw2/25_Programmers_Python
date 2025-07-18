def solution(lines):
    line = [0] * 201  # 좌표 -100 ~ 100 대응 위해 index +100 shift
    for s, e in lines:
        for i in range(s + 100, e + 100):  # 끝점은 포함 안함 (구간 길이니까)
            line[i] += 1
    return sum(1 for x in line if x >= 2)