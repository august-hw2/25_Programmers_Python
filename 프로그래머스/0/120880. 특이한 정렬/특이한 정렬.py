def solution(numlist, n):

    ans = [(abs(n-i), -i) for i in numlist]
    ans.sort()

    return [-i for _, i in ans]