def solution(score):

    avg = [sum(i)/2 for i in score]
    sort_avg = sorted(avg, reverse=True)

    ans = [] #등수

    for i in avg:
        ans.append(sort_avg.index(i)+1)

    return ans