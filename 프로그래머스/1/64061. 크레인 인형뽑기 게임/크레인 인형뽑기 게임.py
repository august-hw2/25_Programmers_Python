from collections import deque

def solution(board, moves):
    answer = 0
    
    # 열 단위로 전치 후, 0 제외 및 deque 생성
    new_board = [
        deque([board[r][c] for r in range(len(board)) if board[r][c] != 0])
        for c in range(len(board[0]))
    ]
        
    stack = []
    #스택에 하나씩 넣으면서 값 확인하기
    for m in moves:
        col = m-1 # 1, 2, 3, 4, 5 줄이 idx로는 0, 1, 2, 3, 4이기 때문
        if new_board[col]: #비어 있지 않을 때
            doll = new_board[col].popleft() #맨 위 인형 뽑기
            if stack and stack[-1] == doll:
                stack.pop()
                answer += 2 #같은 인형 2개
            else:
                stack.append(doll)

    return answer