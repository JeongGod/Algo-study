from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    cands = [[] for _ in range(len(course))]
    for order in orders:
        for idx, course_cnt in enumerate(course):
            order = list(order)
            order.sort()
            comb = combinations(order, course_cnt)
            cands[idx] += comb

    for cand in cands:
        if cand:
            count = Counter(cand)
            max_value = max(count.values())
            if max_value > 1:
                tmp = filter(lambda x: x[1] == max_value, count.items())
                answer += [key for key, value in tmp]

    for idx, elm in enumerate(answer):
        answer[idx] = "".join(elm)
    answer.sort()

    return answer
