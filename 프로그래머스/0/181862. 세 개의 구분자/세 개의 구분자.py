import re
def solution(myStr):
    return [x for x in re.split(r'[abc]', myStr) if x] or ["EMPTY"]