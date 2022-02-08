def solution(id_list, report, k):
    answer = {}
    report_list = {}

    for id in id_list:
        answer[id] = 0
        report_list[id] = set()

    for case in report:
        reporter, target = case.split()
        report_list[target].add(reporter)

    for result in report_list:
        if len(report_list[result]) >= k:
            for reporter in report_list[result]:
                answer[reporter] += 1

    return list(answer.values())
