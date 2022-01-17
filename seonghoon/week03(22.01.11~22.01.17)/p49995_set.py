from itertools import accumulate
from typing import List, Set


def solution(cookies: List[int]) -> int:
    answer: int = 0

    for m in range(len(cookies) - 1):
        left: Set[int] = set(accumulate(reversed(cookies[: m + 1])))
        right: Set[int] = set(accumulate(cookies[m + 1 :]))
        common: Set[int] = left & right

        if common:
            answer = max(answer, *common)

    return answer


# Reference
# 다른 사람 풀이 - 홍성수 , 박상희 , 남상민

# 3
print(solution([1, 1, 2, 3]))
# 0
print(solution([1, 2, 4, 5]))
