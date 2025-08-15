def solution(board, h, w):
    answer = 0

    # 찾아야하는 값 색상 변수에 저장하기
    color = board[h][w]
    H, W = len(board), len(board[0])

    # 상
    if h - 1 >= 0 and board[h - 1][w] == color:
        answer += 1

    # 하
    if h + 1 < H and board[h + 1][w] == color:
        answer += 1

    # 좌
    if w - 1 >= 0 and board[h][w - 1] == color:
        answer += 1

    # 우
    if w + 1 < W and board[h][w + 1] == color:
        answer += 1

    return answer

    return answer