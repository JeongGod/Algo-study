import bisect
import itertools
from collections import defaultdict
from typing import DefaultDict, List


def get_case_list(lang: str, job: str, career: str, food: str) -> List[str]:
    case_list: List[str] = []
    for key in itertools.product([lang, "-"], [job, "-"], [career, "-"], [food, "-"]):
        case_list.append("".join(key))
    return case_list


def solution(info: List[str], query: List[str]):
    info_dict: DefaultDict[str, List[int]] = defaultdict(list)

    for string in info:
        lang, job, career, food, score = string.split()
        for case in get_case_list(lang, job, career, food):
            info_dict[case].append(int(score))

    for key in info_dict.keys():
        info_dict[key].sort()

    answer: List[int] = []
    for string in query:
        splitted = string.split()
        key = splitted[0] + splitted[2] + splitted[4] + splitted[6]
        answer.append(
            len(info_dict[key]) - bisect.bisect_left(info_dict[key], int(splitted[7]))
        )

    return answer


# [1,1,1,1,2,4]
print(
    solution(
        [
            "java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50",
        ],
        [
            "java and backend and junior and pizza 100",
            "python and frontend and senior and chicken 200",
            "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150",
            "- and - and - and chicken 100",
            "- and - and - and - 150",
        ],
    )
)
