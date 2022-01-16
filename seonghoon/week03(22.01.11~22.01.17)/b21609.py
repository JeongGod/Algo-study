import sys
from collections import deque


BLANK = -2
MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]
input = sys.stdin.readline


def isrange(y: int, x: int) -> bool:
    return 0 <= y < n and 0 <= x < n


def getgroup(
    y: int, x: int, normal: int, board: list[list[int]]
) -> tuple[int, list[tuple[int, int]]]:
    rainbow: int = 0
    blocks: list[tuple[int, int]] = []
    que: deque[tuple[int, int]] = deque()
    visited: list[list[bool]] = [[False for _ in range(n)] for _ in range(n)]

    blocks.append((y, x))
    que.append((y, x))
    visited[y][x] = True
    checked[y][x] = True

    while que:
        cury, curx = que.popleft()

        for movey, movex in MOVES:
            nexty: int = cury + movey
            nextx: int = curx + movex

            if not isrange(nexty, nextx):
                continue
            if visited[nexty][nextx]:
                continue
            if board[nexty][nextx] != 0 and board[nexty][nextx] != normal:
                continue

            blocks.append((nexty, nextx))
            que.append((nexty, nextx))
            visited[nexty][nextx] = True
            if board[nexty][nextx] == 0:
                rainbow += 1
            if board[nexty][nextx] == normal:
                checked[nexty][nextx] = True

    return rainbow, blocks


def getmaxgroup(board: list[list[int]]) -> tuple[int, list[tuple[int, int]]]:
    global checked
    checked = [[False for _ in range(n)] for _ in range(n)]

    cnt: int = -1
    rainbow: int = -1
    group: list[tuple[int, int]] = []

    for y, row in enumerate(board):
        for x, elem in enumerate(row):
            if elem <= 0 or checked[y][x]:
                continue

            _rainbow, _group = getgroup(y, x, elem, board)
            _cnt: int = len(_group)

            if _cnt > cnt or (_cnt == cnt and _rainbow >= rainbow):
                cnt = _cnt
                rainbow = _rainbow
                group = _group[:]

    return cnt, group


def removegroup(
    group: list[tuple[int, int]], board: list[list[int]]
) -> list[list[int]]:
    removed: list[list[int]] = [[board[y][x] for x in range(n)] for y in range(n)]
    for y, x in group:
        removed[y][x] = BLANK
    return removed


def fallblocks(board: list[list[int]]) -> list[list[int]]:
    fallen: list[list[int]] = [[BLANK for _ in range(n)] for _ in range(n)]

    for x in range(n):
        fptr: int = n - 1
        for y in range(n - 1, -1, -1):
            if board[y][x] == BLANK:
                continue
            if board[y][x] == -1:
                fptr = y
            fallen[fptr][x] = board[y][x]
            fptr -= 1

    return fallen


def turn(board: list[list[int]]) -> list[list[int]]:
    turned: list[list[int]] = [[BLANK for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            turned[y][x] = board[x][n - y - 1]
    return turned


def play(board: list[list[int]]) -> int:
    score: int = 0

    while True:
        b, group = getmaxgroup(board)
        if b < 2:
            break

        score += b * b
        board = removegroup(group, board)
        board = fallblocks(board)
        board = turn(board)
        board = fallblocks(board)

    return score


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    print(play(board))
