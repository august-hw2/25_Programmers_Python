def solution(keyinput, board):
    x, y = 0, 0

    m_x = board[0]//2
    m_y = board[1]//2

    for key in keyinput:
        if key == "up" and y < m_y:
            y += 1
        elif key == "down" and y > -m_y:
            y -= 1
        elif key == "right" and x < m_x:
            x += 1
        elif key == "left" and x > -m_x:
            x -= 1

    return [x, y]