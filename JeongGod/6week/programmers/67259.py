from collections import deque
from typing import List

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check(x : int, y : int) -> bool:
    if not (0 <= x < N and 0 <= y < N):
        return False
    if a_board[x][y] == 1:
        return False
    return True

def bfs(x : int, y : int) -> int:
    visited = [[[1e9, 1e9, 1e9, 1e9] for _ in range(N)] for _ in range(N)]
    for i in range(4):
        visited[0][0][i] = 0

    dq = deque([(x, y, 0, 5)])
    while dq:
        cx, cy, cost, go = dq.popleft()

        for i in range(4):
            
            nx, ny = cx + dx[i], cy + dy[i]
            if not check(nx, ny):
                continue
            # 직선이거나 처음시작이라면
            if i == go or go == 5:
                new_cost = cost + 100
            # 코너라면
            else:
                new_cost = cost + 600
            # 최소값으로 이동하자.
            if visited[nx][ny][i] <= new_cost:
                continue

            visited[nx][ny][i] = new_cost
            dq.append((nx, ny, new_cost, i))

    return min(visited[N-1][N-1])

def solution(board : List[List[int]]):
    global N, a_board

    a_board = board
    N = len(board)

    return bfs(0, 0)
