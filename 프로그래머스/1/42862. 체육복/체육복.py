def solution(n, lost, reserve):

    #오름차순 정렬
    lost.sort()
    reserve.sort()

    #중복 제거
    for idx in reserve[:]:
        if idx in lost:
            lost.remove(idx)
            reserve.remove(idx)

    #체육복 빌려주기
    for r in reserve:
        if r-1 in lost: #앞쪽 여유분 확인
            lost.remove(r - 1)
        elif r+1 in lost: #뒷쪽 여유분 확인
            lost.remove(r + 1)

    return n - len(lost)