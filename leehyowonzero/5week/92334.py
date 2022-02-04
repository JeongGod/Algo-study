from collections import defaultdict

def solution(id_list, report, k):
    answer = defaultdict(int) # 정답 딕트 만들기
    for el in id_list:
        answer[el] = 0
        
    reported_id_list = defaultdict(set) # 신고당한 아이디 리스트 초기화 및 갱신, 중복 신고를 막기위해 key값은 set자료구조로 저장
    for case in report:
        fm, to = case.split(' ')
        reported_id_list[to] |= {fm}
        
    for reported_id  in reported_id_list: # 조건이 만족되면 정답 딕트에 적용
        if(len(reported_id_list[reported_id]) >= k):
            for el in reported_id_list[reported_id]:
                answer[el] += 1
    return list(answer.values())