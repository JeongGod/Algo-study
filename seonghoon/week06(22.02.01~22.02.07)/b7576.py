import sys
from collections import deque


MAX = sys.maxsize
MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]
input = sys.stdin.readline


def find_ripened_tomatoes(board: list[list[int]]) -> list[tuple[int, int]]:
    ripened_tomatoes: list[tuple[int, int]] = []
    for x, row in enumerate(board):
        for y, elem in enumerate(row):
            if elem == 1:
                ripened_tomatoes.append((x, y))
    return ripened_tomatoes


def isrange(x: int, y: int) -> bool:
    return 0 <= x < n and 0 <= y < m


def ripen_tomatoes(board: list[list[int]]) -> list[list[int]]:
    que: deque[tuple[int, int]] = deque()
    times: list[list[int]] = [
        [0 if board[x][y] == -1 else MAX for y in range(m)] for x in range(n)
    ]

    ripened_tomatoes = find_ripened_tomatoes(board)
    for x, y in ripened_tomatoes:
        que.append((x, y))
        times[x][y] = 0

    while que:
        x, y = que.popleft()

        for movex, movey in MOVES:
            nextx: int = x + movex
            nexty: int = y + movey

            if not isrange(nextx, nexty):
                continue
            if board[nextx][nexty] == -1:
                continue
            if times[nextx][nexty] != MAX:
                continue

            que.append((nextx, nexty))
            times[nextx][nexty] = times[x][y] + 1

    return times


if __name__ == "__main__":
    m, n = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    times = ripen_tomatoes(board)
    maxtime = max(map(max, times))
    print(maxtime if maxtime != MAX else -1)
