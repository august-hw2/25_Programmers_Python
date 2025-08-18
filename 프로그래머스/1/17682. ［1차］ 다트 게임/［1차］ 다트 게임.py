# *(스타상) -> 앞 점수 2배
# #(아차상) -> 앞 점수 마이너스로
def solution(dartResult):

    # single, double, triple 영역 별 점수 제곱값
    board = {'S': 1, 'D': 2, 'T': 3}

    idx = 0
    answer = []

    # 구분해서 점수 계산하기
    for i in range(len(dartResult)):
        op = dartResult[i]
        if op in board:
            answer.append((int(dartResult[idx:i]) ** board[op]))
        elif op == '*':
            answer[-2:] = [x * 2 for x in answer[-2:]]
        elif op == '#':
            answer[-1] = -answer[-1]

        # 숫자가 아니면 다음 인덱스로
        if not op.isnumeric():
            idx = i + 1

    return sum(answer)