def solution(X, Y):

    cnt_x = [0]*10
    cnt_y = [0]*10
    
    # 각 문자열에서 숫자 등장 횟수 세기
    for x in X: cnt_x[ord(x) - 48] += 1
    for y in Y: cnt_y[ord(y) - 48] += 1

    answer = []
    
    # 두 문자열의 공통 숫자를 큰 숫자부터 이어서 붙이기
    # 9부터 역순으로 내려오며, 두 문자열에서 해당 숫자가 공통으로 있는 만큼 결과에 추가
    for i in range(9, -1, -1):
        tmp = min(cnt_x[i], cnt_y[i])   # 공통 개수
        if tmp:
            answer.append(str(i)*tmp)

    if not answer:
        return "-1"

    result = "".join(answer)

    return "0" if result[0] == "0" else result