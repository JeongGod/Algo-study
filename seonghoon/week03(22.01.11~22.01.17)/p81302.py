from typing import List


ADJS = [(-1, 0), (0, 1), (1, 0)]
ADJ_NEXTS = [[(-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(1, 0), (0, 1)]]


def isrange(y: int, x: int) -> bool:
    return 0 <= y < 5 and 0 <= x < 5


def check_adjnexts(y: int, x: int, idx: int, board: List[str]) -> bool:
    for movey, movex in ADJ_NEXTS[idx]:
        nexty: int = y + movey
        nextx: int = x + movex

        if not isrange(nexty, nextx):
            continue
        if board[nexty][nextx] == "P":
            return True

    return False


def check_adjs(y: int, x: int, board: List[str]) -> bool:
    for idx, (movey, movex) in enumerate(ADJS):
        adjy: int = y + movey
        adjx: int = x + movex

        if not isrange(adjy, adjx):
            continue
        if board[adjy][adjx] == "X":
            continue
        if board[adjy][adjx] == "P":
            return True
        if check_adjnexts(adjy, adjx, idx, board):
            return True

    return False


def isdistanced(board: List[str]) -> bool:
    for y, row in enumerate(board):
        for x, elem in enumerate(row):
            if elem == "P" and check_adjs(y, x, board):
                return False
    return True


def solution(places: List[List[str]]) -> List[int]:
    return [int(isdistanced(board)) for board in places]


# [1, 0, 1, 1, 1]
print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    )
)
