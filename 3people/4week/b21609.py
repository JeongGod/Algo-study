from collections import deque

def findBlockGroup(x, y, color):
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  dq = deque()
  dq.append([x,y])
  block_cnt, rainbow_cnt = 1, 0
  blocks = [[x,y]]
  rainbows = []

  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      # 보드 범위 안 and 전 칸의 색과 같음 and 방문하지 않음
      if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == color and not visited[nx][ny]:
        visited[nx][ny] = True
        dq.append([nx, ny])
        blocks.append([nx,ny])
        block_cnt += 1

      # 보드 범위 안 and 무지개 블록 and 방문하지 않음
      if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0 and not visited[nx][ny]:
        visited[nx][ny] = True
        dq.append([nx, ny])
        rainbows.append([nx, ny])
        block_cnt += 1
        rainbow_cnt += 1

  for x,y in rainbows:
    visited[x][y] = False

  return [block_cnt, rainbow_cnt, blocks + rainbows]

def removeBlock(candidate):
  for x, y in candidate:
    board[x][y] = -999

def gravity(board):
  for x in range(N-2, -1, -1):
    for y in range(N):
      if board[x][y] > -1:
        curr = x
        while True:
          if 0 <= curr + 1 < N and board[curr+1][y] == -999:
            board[curr+1][y] = board[curr][y]
            board[curr][y] = -999
            curr += 1
          else:
            break
          
def counterClock(board):
  res = [[0] * N for _ in range(N)]
  for x in range(N):
    for y in range(N):
      res[N-y-1][x] = board[x][y]
  return res

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
score = 0

while True:
  visited = [[False] * N for _ in range(N)]
  able = []
  for x in range(N):
    for y in range(N):
      if board[x][y] > 0 and not visited[x][y]:
        visited[x][y] = True
        find_info = findBlockGroup(x, y, board[x][y])
        if find_info[0] >= 2:
          able.append(find_info)
  able.sort(reverse=True)

  if not able:
    break

  removeBlock(able[0][2])

  score += able[0][0] ** 2

  gravity(board)

  board = counterClock(board)

  gravity(board)

print(score)
