def solution(num, total):

    first = (2 * total - num * (num - 1)) // (2 * num)
    return [first + i for i in range(num)]

'''
등차수열의 합 공식 이용
총합 = 항의 개수 * (첫번째 항 + 마지막 항) / 2
total = num * ( a + a + (num-1) ) / 2
total = num * ( 2a + num - 1 ) / 2

-> a를 구하는 공식으로 유도하면,
2 * total = num * ( 2a + num - 1 )
(2 * total) / num = 2a + num - 1
2a = 1 - num + (2 * total) / num
a = ((2 * total)/num + 1 - num) / 2

-> 깔끔하게 표현하면
a = (2 * total - num * (num - 1)) // (2 * num)

'''