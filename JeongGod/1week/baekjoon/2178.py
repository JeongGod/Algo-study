import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = list(list(input()) for _ in range(N))

dq = deque([(0, 0)])
dist = [(0, 1), (0, -1), (1, 0), (-1, 0)]
board[0][0] = 0
while dq:
    x, y = dq.popleft()
    if x == N-1 and y == M-1:
        print(board[x][y] + 1)
        break
    for gx, gy in dist:
        nx, ny = x + gx, y + gy
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == "1":
            board[nx][ny] = board[x][y] + 1
            dq.append((nx, ny))
