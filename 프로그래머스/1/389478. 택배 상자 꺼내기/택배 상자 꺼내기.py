def solution(n, w, num):
    # 1. target_num의 좌표 찾기 함수화
    def get_coords(val, width):
        row = (val - 1) // width
        col = (val - 1) % width
        if row % 2 == 1: # 홀수 행은 역방향
            col = (width - 1) - col
        return row, col

    target_row, target_col = get_coords(num, w)
    max_row = (n - 1) // w
    
    count = 0
    # 2. target_row부터 마지막 row까지 순회하며 해당 열에 박스가 있는지 계산
    for r in range(target_row, max_row + 1):
        # 해당 행(r)에서 target_col에 위치해야 할 실제 번호를 역산하거나
        # 해당 행의 유효 범위를 체크
        
        # 행 r에서의 열 c의 인덱스 위치(0~w-1)는:
        # r이 짝수면 c, r이 홀수면 (w-1-c)
        logical_col = target_col if r % 2 == 0 else (w - 1) - target_col
        actual_val = r * w + logical_col + 1
        
        if actual_val <= n:
            count += 1
            
    return count