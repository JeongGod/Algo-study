from typing import List, Tuple
from itertools import permutations


def count(k: int, iters: Tuple[int, ...], dungeons: List[List[int]]) -> int:
    cnt: int = 0

    for dungeon_idx in iters:
        need, use = dungeons[dungeon_idx]

        if need > k:
            break

        k -= use
        cnt += 1

    return cnt


def solution(k: int, dungeons: List[List[int]]):
    answer = -1

    for pmt in permutations(range(len(dungeons))):
        answer = max(answer, count(k, pmt, dungeons))

    return answer


# 3
print(solution(80, [[80, 20], [50, 40], [30, 10]]))
