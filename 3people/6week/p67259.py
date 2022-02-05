from collections import deque
import sys
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(board, d):
  n = len(board)
  price = [[sys.maxsize] * n for _ in range(n)]
  price[0][0] = 0
  dq = deque()
  dq.append((0, 0, 0, d))
  
  while dq:
    x, y, cost, d = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      nd = i
      if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
        if nd == d:
          nc = cost + 100
        else:
          nc = cost + 600
        if nc < price[nx][ny]:
          price[nx][ny] = nc
          dq.append((nx, ny, nc, nd))
  return price[-1][-1]
  
def solution(board):
  answer = min(bfs(board, 1), bfs(board, 3))
  return answer