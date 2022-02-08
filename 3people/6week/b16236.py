import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
  visited = [[False] * n for _ in range(n)]
  dist = [[0] * n for _ in range(n)]
  dq = deque()
  dq.append([x, y])
  visited[x][y] = True
  can_eat = []
  
  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
        if board[nx][ny] <= shark:
          visited[nx][ny] = True
          dq.append([nx, ny])
          dist[nx][ny] = dist[x][y] + 1
          if board[nx][ny] < shark and board[nx][ny] != 0:
            can_eat.append([nx, ny, dist[nx][ny]])
  return sorted(can_eat, key=lambda x: (x[2], x[0], x[1]))

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
shark_x, shark_y = 0, 0
shark = 2
answer = 0
eat_cnt = 0

for i in range(n):
  for j in range(n):
    if board[i][j] == 9:
      shark_x, shark_y = i, j

while True:
  move_info = bfs(shark_x, shark_y)
  if len(move_info) == 0:
    break
  nx, ny, dist = move_info.pop(0)
  answer += dist
  board[shark_x][shark_y] = 0
  board[nx][ny] = 0
  shark_x, shark_y = nx, ny
  eat_cnt += 1
  if eat_cnt == shark:
    shark += 1
    eat_cnt = 0
print(answer)