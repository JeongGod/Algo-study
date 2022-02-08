from collections import deque
import sys
from typing import Deque, List, Tuple


INIT_FEE = sys.maxsize
MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def isrange(x: int, y: int, n: int) -> bool:
    return 0 <= x < n and 0 <= y < n


def solution(board: List[List[int]]) -> int:
    n: int = len(board)
    que: Deque[Tuple[int, int, int]] = deque()
    fees: List[List[List[int]]] = [
        [[INIT_FEE for _ in range(4)] for _ in range(n)] for _ in range(n)
    ]

    que.append((0, 0, 1))
    que.append((0, 0, 2))
    fees[0][0][1] = 0
    fees[0][0][2] = 0

    while que:
        x, y, dir = que.popleft()

        for movedir, (movex, movey) in enumerate(MOVES):
            nextx: int = x + movex
            nexty: int = y + movey
            nextfee: int = fees[x][y][dir] + (100 if dir == movedir else 600)

            if not isrange(nextx, nexty, n):
                continue
            if board[nextx][nexty] == 1:
                continue
            if fees[nextx][nexty][movedir] <= nextfee:
                continue

            que.append((nextx, nexty, movedir))
            fees[nextx][nexty][movedir] = nextfee

    return min(fees[n - 1][n - 1])


# 900
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
# 3800
print(
    solution(
        [
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
)
# 2100
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
# 3200
print(
    solution(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
    )
)
