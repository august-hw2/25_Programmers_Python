def solution(board, h, w):
    answer = 0

    # 찾아야하는 값 색상 변수에 저장하기
    color = board[h][w]
    H, W = len(board), len(board[0])

    #상 하 좌 우 순서로 확인 + 리스트 크기 범위인지 확인
    for idxh, idxw in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nh, nw = h + idxh, w + idxw
        if 0 <= nh < H and 0 <= nw < W and board[nh][nw] == color:
            answer += 1

    return answer