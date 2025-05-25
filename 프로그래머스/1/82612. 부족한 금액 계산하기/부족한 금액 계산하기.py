def solution(price, money, count):
    #등차수열의 합 공식 이용
    sn = (count*((2*price) + (count-1)*price))//2

    return sn-money if sn >= money else 0