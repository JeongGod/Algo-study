from typing import List, Tuple


def getmins(balloons: List[Tuple[int, int]]) -> List[int]:
    minballon: int = 2_000_000_000
    mins: List[int] = [-1 for _ in range(len(balloons))]

    for idx, balloon in balloons:
        minballon = min(minballon, balloon)
        mins[idx] = minballon

    return mins


def solution(a: List[int]) -> int:
    mins_from_left: List[int] = getmins(list(enumerate(a)))
    mins_from_right: List[int] = getmins(list(reversed(list(enumerate(a)))))

    answer: int = sum(
        int(balloon <= left or balloon <= right)
        for balloon, left, right in zip(a, mins_from_left, mins_from_right)
    )
    return answer


# 3
print(solution([9, -1, -5]))
# 6
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
