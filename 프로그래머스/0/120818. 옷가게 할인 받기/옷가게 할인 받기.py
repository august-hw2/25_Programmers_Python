def solution(price):
    if price >= 500000:
        return int(price*0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    else: #할인받지 못하는 가격은 그대로 출력
        return price