def solution(wallet, bill):
    cnt = 0 # 지폐 접은 횟수

    # 지갑, 지폐의 가로/세로 길이 저장
    w1, w2 = wallet[0], wallet[1]
    b1, b2 = bill[0], bill[1]

    # 기존 위치 그대로 비교 or 90도 돌려서 비교
    while min(w1, w2) < min(b1, b2) or max(w1, w2) < max(b1, b2):

        # 이후, 긴 쪽 길이 접기 => 나누기 2 (이 때, 홀수라면 소수점 버리기)
        if b1 >= b2:
            b1 //= 2
        else:
            b2 //= 2

        cnt += 1

    return cnt