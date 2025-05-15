from collections import Counter

def solution(spell, dic):
    spell_cnt = Counter(spell)

    for i in dic:
        if Counter(i) == spell_cnt:
            return 1
    return 2