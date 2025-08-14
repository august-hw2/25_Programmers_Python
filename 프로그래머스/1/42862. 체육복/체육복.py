def solution(n, lost, reserve):
    # 중복 제거
    lost = set(lost)
    reserve = set(reserve)

    # 1) 여벌도 잃어버린 학생 정리 (자기 옷 먼저 사용)
    inter = lost & reserve
    lost -= inter
    reserve -= inter

    # 2) 빌려주기: 왼쪽 먼저, 안 되면 오른쪽
    for r in sorted(reserve):
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)

    return n - len(lost)