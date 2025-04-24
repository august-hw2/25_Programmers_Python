import operator
def solution(ineq, eq, n, m):
    ops = {
        '>=': operator.ge,  # greater than or equal
        '<=': operator.le,  # less than or equal
        '>': operator.gt,  # greater than
        '<': operator.lt  # less than
    }
    key = ineq + eq.replace('!', '')
    return int(ops[key](n, m))