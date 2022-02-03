from collections import deque
from typing import Deque, Tuple, List


def solution(priorities: List[int], location: int) -> int:
    print_que: Deque[Tuple[int, int]] = deque(
        [(idx, priority) for idx,  priority in enumerate(priorities)])
    print_idx: int = -1
    print_turn: int = 0

    while print_idx != location and print_que:
        idx, curr = print_que.popleft()

        if curr < max(priorities):
            print_que.append((idx, curr))
        else:
            print_turn += 1
            print_idx = idx
            priorities[priorities.index(curr)] = 0

    return print_turn
