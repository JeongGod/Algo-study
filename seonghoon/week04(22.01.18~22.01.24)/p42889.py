from collections import Counter
from typing import Dict, List, Tuple


def solution(N: int, stages: List[int]) -> List[int]:
    counter: Counter[int] = Counter(stages)
    user: int = len(stages)

    failure_rates: Dict[int, float] = {stage: 0 for stage in range(1, N + 1)}
    for stage in range(1, N + 1):
        if user <= 0:
            break
        failure_rates[stage] = counter[stage] / user
        user -= counter[stage]

    sorted_rates: List[Tuple[int, float]] = sorted(
        failure_rates.items(), key=lambda x: (-x[1], x[0])
    )

    return list(map(lambda x: x[0], sorted_rates))


# [3,4,2,1,5]
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# [4,1,2,3]
print(solution(4, [4, 4, 4, 4, 4]))
