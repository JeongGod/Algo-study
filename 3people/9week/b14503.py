# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 0 3
# 1 0
# 2 1
# 3 2
n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def clean(r, c, d):
  global answer
  if board[r][c] == 0:
    board[r][c] = 2
    answer += 1
  for _ in range(4):
    nd = (d + 3) % 4 # 왼쪽으로 방향 돌리기
    nx, ny = r + dx[nd], c + dy[nd]
    if board[nx][ny] == 0:
      clean(nx, ny, nd)
      return
    d = nd # 청소못하면 방향 돌림
  nd = (d + 2) % 4 # 후진하기 위해 뒤로 방향 돌리기
  nx, ny = r + dx[nd], c + dy[nd]
  if board[nx][ny] == 1:
    return
  clean(nx, ny, d) # 방향을 유지한 채로 뒤로 이동

answer = 0
clean(r, c, d)
print(answer)