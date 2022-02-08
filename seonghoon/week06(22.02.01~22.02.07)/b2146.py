import sys
from collections import deque


MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]
input = sys.stdin.readline


def isrange(x: int, y: int) -> bool:
    return 0 <= x < n and 0 <= y < n


def get_lands(x: int, y: int, island: int) -> set[tuple[int, int]]:
    lands: set[tuple[int, int]] = set()
    que: deque[tuple[int, int]] = deque()

    que.append((x, y))
    lands.add((x, y))
    board[x][y] = island

    while que:
        x, y = que.popleft()

        for movex, movey in MOVES:
            nextx: int = x + movex
            nexty: int = y + movey

            if not isrange(nextx, nexty):
                continue
            if board[nextx][nexty] == 0:
                continue
            if (nextx, nexty) in lands:
                continue

            que.append((nextx, nexty))
            lands.add((nextx, nexty))
            board[nextx][nexty] = island

    return lands


def get_bridge_length(lands: set[tuple[int, int]], island: int) -> int:
    length: int = 0
    que: deque[tuple[int, int]] = deque()
    visited: list[list[bool]] = [[False for _ in range(n)] for _ in range(n)]

    for x, y in lands:
        que.append((x, y))
        visited[x][y] = True

    while que:
        for _ in range(len(que)):
            x, y = que.popleft()

            for movex, movey in MOVES:
                nextx: int = x + movex
                nexty: int = y + movey

                if not isrange(nextx, nexty):
                    continue
                if board[nextx][nexty] == island:
                    continue
                if visited[nextx][nexty]:
                    continue

                if board[nextx][nexty] > 0:
                    return length

                que.append((nextx, nexty))
                visited[nextx][nexty] = True

        length += 1

    return -1


def solve() -> int:
    island: int = 2
    length: int = sys.maxsize

    for x, row in enumerate(board):
        for y, elem in enumerate(row):
            if elem == 1:
                lands = get_lands(x, y, island)
                length = min(length, get_bridge_length(lands, island))
                island += 1

    return length


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    print(solve())
