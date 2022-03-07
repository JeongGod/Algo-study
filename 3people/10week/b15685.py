dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
curves = [list(map(int, input().split())) for _ in range(n)]
board = [[0] * 101 for _ in range(101)]

for curve in curves:
  x, y, w, g = curve[0], curve[1], curve[2], curve[3]
  board[x][y] = 1
  move = [w]

  for _ in range(g):
    temp = list(map(lambda x: (x + 1) % 4, move[::-1]))
    move = move + temp
  
  for m in move:
    nx, ny = x + dx[m], y + dy[m]
    board[nx][ny] = 1
    x, y = nx, ny

ans = 0
for i in range(100):
  for j in range(100):
    if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
      ans += 1

print(ans)
