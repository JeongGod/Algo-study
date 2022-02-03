from collections import deque
import sys

input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def rotate(board, i, j, level):
  row = []
  for y in range(j, j+2**level):
    el = [board[x][y] for x in range(i+2**level-1, i-1, -1)]
    row.append(el)

  for x in range(2**level):
    for y in range(2**level):
      board[i+x][j+y] = row[x][y]

def melt(board):
  cand = []
  for x in range(2**N):
    for y in range(2**N):
      cnt = 0
      for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i]
        if 0 <= nx < 2**N and 0 <= ny < 2**N and board[nx][ny] != 0:
          cnt += 1
      if cnt < 3 and board[x][y] != 0:
          cand.append([x, y])
  for x, y in cand:
    board[x][y] -= 1

def count_group(board):
  answer = 0
  maxx = 0
  for x in range(2**N):
    for y in range(2**N):
      answer += board[x][y]
      if not(0 <= x < 2**N and 0 <= y < 2**N) or board[x][y] == 0 or visited[x][y]:
        continue
      visited[x][y] = True
      maxx = max(maxx, dfs(x, y, visited))
  return answer, maxx

def dfs(x, y, visited):
  dq = deque()
  dq.append([x,y])
  width = 0
  while dq:
    x, y = dq.popleft()
    width += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < 2**N and 0 <= ny < 2**N and board[nx][ny] != 0 and not visited[nx][ny]:
        visited[nx][ny] = True
        dq.append([nx, ny])
  return width

def firestorm(board, level):
  for i in range(0, 2**N, 2**level):
    for j in range(0, 2**N, 2**level):
      rotate(board, i, j, level)
  melt(board)

N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))
visited = [[False] * 2**N for _ in range(2**N)]

for level in L:
  firestorm(board, level)
answer, maxx = count_group(board)
print(answer, maxx, sep='\n')