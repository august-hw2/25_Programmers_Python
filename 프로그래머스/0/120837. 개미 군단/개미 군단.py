def solution(hp):
    #장군개미 5, 병정 개미 3, 일개미 1
    return (hp//5)+(hp%5//3)+(hp%5%3//1)