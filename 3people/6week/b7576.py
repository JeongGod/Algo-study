import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dq = deque()

def bfs():
  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
        dq.append([nx, ny])
        board[nx][ny] = board[x][y] + 1

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n):
  for j in range(m):
    if board[i][j] == 1:
      dq.append([i, j])

bfs()
for b in board:
  for el in b:
    if el == 0:
      print(-1)
      exit(0)
  answer = max(answer, max(b))
print(answer - 1)