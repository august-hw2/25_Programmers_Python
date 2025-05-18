from collections import Counter

def solution(array):

    if not array:
        return -1

    cnt = Counter(array)
    most_cnt = cnt.most_common(2) #가장 많이 나온 값 2개

    if len(most_cnt) == 1 or most_cnt[0][1] > most_cnt[1][1]:
        return most_cnt[0][0]
    else:
        return -1