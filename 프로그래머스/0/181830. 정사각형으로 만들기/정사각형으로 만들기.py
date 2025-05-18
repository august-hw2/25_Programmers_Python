def solution(arr):

    row = len(arr)
    col = len(arr[0])

    if row > col: #행 > 열
        for i in arr:
            i.extend([0]*(row-col))
    elif row < col: #행 < 열
        for _ in range(col-row):
            arr.append([0]*col)

    return arr