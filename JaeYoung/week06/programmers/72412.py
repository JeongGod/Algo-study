from bisect import bisect_left
from collections import defaultdict
from typing import DefaultDict, List, Set


def combi_condition(conditions: List[str]) -> Set[str]:
    possible_conditions = set()
    for language in ["cpp", "java", "python"]:
        skeleton = conditions[:]
        if conditions[0] == "-":
            skeleton[0] = language
        for job in ["backend", "frontend"]:
            if conditions[1] == "-":
                skeleton[1] = job
            for career in ["junior", "senior"]:
                if conditions[2] == "-":
                    skeleton[2] = career
                for food in ["chicken", "pizza"]:
                    if conditions[3] == "-":
                        skeleton[3] = food
                    possible_conditions.add("".join(skeleton))
    return possible_conditions


def solution(infos: List[str], queries: List[str]):
    answer: List[int] = []
    applicant_dict: DefaultDict[str, List[int]] = defaultdict(list)

    for info in infos:
        score = int(info.split()[-1])
        applicant = ''.join(info.split()[0:-1])
        applicant_dict[applicant].append(score)

    for _, items in applicant_dict.items():
        items.sort()

    for query in queries:
        cnt = 0
        find_score = int(query.replace(
            "and", "").replace("  ", " ").split()[-1])
        conditions = query.replace("and", "").replace("  ", " ").split()[0:-1]
        possible_conditions = combi_condition(conditions)

        for conditions in possible_conditions:
            if conditions in applicant_dict:
                cnt += (len(applicant_dict[conditions]) -
                        bisect_left(applicant_dict[conditions], find_score))
        answer.append(cnt)
    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
                "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
