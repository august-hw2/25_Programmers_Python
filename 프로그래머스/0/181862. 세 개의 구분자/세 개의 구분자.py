import re
def solution(myStr):
    tmp = re.split(r'[abc]', myStr)
    res = list(filter(None, tmp))
    return res if res else ["EMPTY"]