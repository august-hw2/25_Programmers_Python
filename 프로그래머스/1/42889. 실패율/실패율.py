def solution(N, stages):
    fail = {} # 스테이지 번호별 실패율을 저장할 딕셔너리

    stages.sort() # 오름차순 정리

    for n in range(1, N+1):
        target = n
        cnt = stages.count(n) # 현재 스테이지에 있는 인원 수

        fail[n] = cnt/len(stages) if stages else 0 # 실패율 계산

        stages = [x for x in stages if x != target] # 클리어 못한 사람 제거

    # 실패율(value) 기준 내림차순, 값이 같으면 key(스테이지) 기준 오름차순
    sorted_fail = sorted(fail.items(), key=lambda x: (-x[1], x[0]))
    # fail.items() -> 딕셔너리의 (스테이지 번호, 실패율) 쌍으로 리스트로 반환
    # x[1]: 실패율, x[0]: 스테이지 번호
    # -x[1]: 실패율 내림차순 정렬 의미

    return [stage for stage, _ in sorted_fail] # 스테이지만 뽑아서 반환
    # sorted_fail은 (스테이지 번호, 실패율) 형태이므로, stage만 추출
