def solution(id_pw, db):
    ans = ''

    for i in db:
        a, b = i
        if id_pw[0] == a:
            if id_pw[1] == b:
                ans = "login"
            else:
                ans = "wrong pw"

    return ans if len(ans) else "fail"
