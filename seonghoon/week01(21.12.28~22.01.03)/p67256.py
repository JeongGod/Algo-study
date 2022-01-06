from typing import List


LEFT = set([1, 4, 7])
CENTER = set([2, 5, 8, 0])
COORDINATES = [
    (3, 1),  # 0
    (0, 0),  # 1
    (0, 1),  # 2
    (0, 2),  # 3
    (1, 0),  # 4
    (1, 1),  # 5
    (1, 2),  # 6
    (2, 0),  # 7
    (2, 1),  # 8
    (2, 2),  # 9
    (3, 0),  # 10, *
    (3, 2),  # 11, #
]


def getdistance(num: int, finger: int) -> int:
    ny, nx = COORDINATES[num]
    fy, fx = COORDINATES[finger]
    return abs(ny - fy) + abs(nx - fx)


def solution(numbers: List[int], hand: str):
    answer: str = ""
    left: int = 10  # *
    right: int = 11  # #

    for num in numbers:
        use_right: bool = True

        if num in LEFT:
            use_right = False
        elif num in CENTER:
            ldist = getdistance(num, left)
            rdist = getdistance(num, right)
            if ldist < rdist or (ldist == rdist and hand == "left"):
                use_right = False

        if use_right:
            answer += "R"
            right = num
        else:
            answer += "L"
            left = num

    return answer


# "LRLLLRLLRRL"
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
# "LRLLRRLLLRR"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
# "LLRLLRLLRL"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
