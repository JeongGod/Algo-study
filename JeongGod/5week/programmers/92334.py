from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_num = defaultdict(int)
    
    for _, b in map(lambda x:x.split(), set(report)):
        report_num[b] += 1
    
    for a, b in map(lambda x:x.split(), set(report)):
        if report_num[b] >= k:
            answer[id_list.index(a)] += 1
    return answer
