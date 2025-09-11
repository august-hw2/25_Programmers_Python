# date = [code, date, maximum, remain] = [코드번호, 제조일, 최대 수량, 현재 수량]
# ext = 어떤 정보를 기준으로 데이터를 뽑아낼지
# val_ext = 뽑아낼 정보의 기준값 (정수)
# sort_by =  정렬 기준 문자열

def solution(data, ext, val_ext, sort_by):
    answer = []
    
    # 정렬 기준 값 -> 인덱스 번호로 설정
    dict = { # 키 (= 정렬 기준) : 값 (= 인덱스)
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    # ext (기준)에 따라서 val_ext 값 보다 작은 데이터만 뽑기
    ext_idx = dict[ext] # 기준 정보 값의 인덱스 값만 저장
    sort_idx = dict[sort_by]


    for i in data:
        if i[ext_idx] < val_ext:
            answer.append(i)

    return sorted(answer, key=lambda x : x[sort_idx])
