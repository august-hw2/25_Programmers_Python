def count(num):

    cnt = []

    for i in range(1, int(num**(1/2) + 1)):
        if num%i==0:
            cnt.append(i)
            if i**2 != num:
                cnt.append(num//i)

    return len(cnt)

def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        j = count(i)
        if j%2: #홀수
            answer -= i
        else: #짝수
            answer += i

    return answer