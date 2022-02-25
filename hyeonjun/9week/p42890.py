from copy import deepcopy
from collections import deque
from itertools import combinations


def solution(relation):
    answer = 0
    comb = deque()
    column_length = len(relation[0])

    key_idx = [i for i in range(column_length)]
    for i in range(1, column_length):
        comb.extend(combinations(key_idx, i))

    while comb:
        target = comb.popleft()
        check_tuple = set()
        for elm in relation:
            tuple_sum = ''
            for idx in target:
                tuple_sum += elm[idx]
            check_tuple.add(tuple_sum)

        copy_comb = deepcopy(comb)
        if len(check_tuple) == len(relation):
            answer += 1
            for idx, elm in enumerate(copy_comb):
                if set(target).issubset(elm):
                    comb.remove(elm)

    return answer
