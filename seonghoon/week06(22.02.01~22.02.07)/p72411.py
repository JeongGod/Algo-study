from collections import Counter
from itertools import combinations
from typing import List


def solution(orders: List[str], course: List[int]):
    answer: List[str] = []
    for length in course:
        order_list: List[str] = []
        for order in orders:
            order_list.extend(
                list("".join(sorted(cbnt)) for cbnt in combinations(order, length))
            )
        common_list = Counter(order_list).most_common()
        answer += [
            menu for menu, cnt in common_list if cnt > 1 and cnt == common_list[0][1]
        ]
    return sorted(answer)


# ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
# ["WX", "XY"]
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
