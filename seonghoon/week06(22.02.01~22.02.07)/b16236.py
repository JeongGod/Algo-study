import sys
from collections import deque


NOT_FOUND = (-1, -1)
MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]
input = sys.stdin.readline


def search_shark() -> tuple[int, int]:
    for x, row in enumerate(board):
        for y, elem in enumerate(row):
            if elem == 9:
                return (x, y)
    return NOT_FOUND


def isrange(x: int, y: int) -> bool:
    return 0 <= x < n and 0 <= y < n


def search_fish(start: tuple[int, int], size: int) -> tuple[tuple[int, int], int]:
    dist: int = 0
    fishes: list[tuple[int, int]] = []
    que: deque[tuple[int, int]] = deque()
    visited: list[list[bool]] = [[False for _ in range(n)] for _ in range(n)]

    startx, starty = start
    que.append((startx, starty))
    visited[startx][starty] = True

    while que and not fishes:
        dist += 1
        for _ in range(len(que)):
            x, y = que.popleft()

            for movex, movey in MOVES:
                nextx: int = x + movex
                nexty: int = y + movey

                if not isrange(nextx, nexty):
                    continue
                if visited[nextx][nexty]:
                    continue
                if board[nextx][nexty] > size:
                    continue

                visited[nextx][nexty] = True
                if board[nextx][nexty] == 0 or board[nextx][nexty] == size:
                    que.append((nextx, nexty))
                else:
                    fishes.append((nextx, nexty))

    if fishes:
        return sorted(fishes)[0], dist
    return NOT_FOUND, dist


def make_empty(point: tuple[int, int]) -> None:
    x, y = point
    board[x][y] = 0


def solve() -> int:
    eaten: int = 0
    size: int = 2
    time: int = 0
    shark = search_shark()
    make_empty(shark)

    while True:
        fish, dist = search_fish(shark, size)
        if fish == NOT_FOUND:
            break

        make_empty(fish)

        shark = fish
        time += dist
        eaten += 1
        if size == eaten:
            size += 1
            eaten = 0

    return time


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    print(solve())
