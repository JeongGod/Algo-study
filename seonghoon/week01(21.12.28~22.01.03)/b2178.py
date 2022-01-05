import sys
from collections import deque


IMP = -1
MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]
input = sys.stdin.readline


def isrange(y: int, x: int) -> bool:
    return 0 <= y < n and 0 <= x < m


def bfs() -> int:
    que: deque[tuple[int, int, int]] = deque()
    visited: list[list[bool]] = [[False for _ in range(m)] for _ in range(n)]

    que.append((0, 0, 1))
    visited[0][0] = True

    while que:
        y, x, cnt = que.popleft()
        next_cnt: int = cnt + 1

        for move_y, move_x in MOVES:
            next_y: int = y + move_y
            next_x: int = x + move_x

            if next_y == n - 1 and next_x == m - 1:
                return next_cnt

            if (
                not isrange(next_y, next_x)
                or visited[next_y][next_x]
                or board[next_y][next_x] == "0"
            ):
                continue

            que.append((next_y, next_x, next_cnt))
            visited[next_y][next_x] = True

    return IMP


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]

    print(bfs())
