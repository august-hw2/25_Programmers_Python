def solution(wallpaper):
    tmp = [] # 파일 위치를 모두 저장할 리스트

    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[0])):
            if wallpaper[x][y] == '#':
                tmp.append([x, y])

    new_tmp = list(map(list, zip(*tmp)))

    print(new_tmp)

    return [min(new_tmp[0]), min(new_tmp[1]), max(new_tmp[0])+1, max(new_tmp[1])+1]