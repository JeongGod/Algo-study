from typing import Set, Tuple


MOVES = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}


def isrange(y: int, x: int) -> bool:
    return -5 <= y <= 5 and -5 <= x <= 5


def solution(dirs: str) -> int:
    cury: int = 0
    curx: int = 0
    paths: Set[Tuple[int, int, int, int]] = set()

    for dir in dirs:
        movey, movex = MOVES[dir]
        nexty: int = cury + movey
        nextx: int = curx + movex

        if not isrange(nexty, nextx):
            continue

        paths.add((cury, curx, nexty, nextx))
        paths.add((nexty, nextx, cury, curx))
        cury, curx = nexty, nextx

    return len(paths) // 2


# 7
print(solution("ULURRDLLU"))
# 7
print(solution("LULLLLLLU"))
