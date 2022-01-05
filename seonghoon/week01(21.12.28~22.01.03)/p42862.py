from typing import List, Set


def solution(n: int, lost: List[int], reserve: List[int]):
    lost_set: Set[int] = set(lost)
    reserve_set: Set[int] = set(reserve)

    common: Set[int] = lost_set & reserve_set
    lost_set.difference_update(common)
    reserve_set.difference_update(common)

    for reserved in reserve_set:
        for borrowed in [reserved - 1, reserved + 1]:
            if borrowed in lost_set:
                lost_set.remove(borrowed)
                break

    return n - len(lost_set)


# 5
print(solution(5, [2, 4], [1, 3, 5]))
# 4
print(solution(5, [2, 4], [3]))
# 2
print(solution(3, [3], [1]))
