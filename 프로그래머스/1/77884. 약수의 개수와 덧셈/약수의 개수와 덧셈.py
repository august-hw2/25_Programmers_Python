def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        # 제곱수인 경우가 해당되면, 무조건 약수 개수가 홀수임
        if int(i ** 0.5) == i ** 0.5:
            answer -= i  # 제곱수면 빼기
        else:
            answer += i  # 아니면 더하기

    return answer