from collections import deque
from typing import Deque, List, Tuple


def solution(bridge_length: int, weight: int, truck_weights: List[int]) -> int:
    prev: int = 1
    total: int = 0
    que: Deque[Tuple[int, int]] = deque()

    for tweight in truck_weights:
        while tweight + total > weight or len(que) >= bridge_length:
            prev, prev_weight = que.popleft()
            total -= prev_weight

        passed_time: int = prev + bridge_length
        if que:
            passed_time = max(que[-1][0] + 1, passed_time)

        total += tweight
        que.append((passed_time, tweight))

    return que[-1][0]


# 8
print(solution(2, 10, [7, 4, 5, 6]))
# 101
print(solution(100, 100, [10]))
# 110
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
# 6
print(solution(1, 10, [1, 2, 3, 7, 8]))
