def solution(board):
    n = len(board)
    danger = set()
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n:
                            danger.add((ni, nj))
    
    return n * n - len(danger)
