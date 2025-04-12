def solution(rsp):
    #rsp -> 가위 2, 바위 0, 보 5
    #값   -> 바위 0, 보 5, 가위 2
    #위 경우에 이기게 됨

    key = dict(zip(['2','0','5'], ['0','5','2']))
    #return ''.join(key[i] for i in rsp) -> 문자열로 반복가능
    return ''.join(key[i] for i in list(rsp))