def find_four(m, n, board):
  s = set()
  for i in range(m-1):
    for j in range(n-1):
      if board[i][j] and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
        s.update({(i,j), (i,j+1), (i+1, j), (i+1, j+1)})
  return s

def pop_four(s, board):
  temp = [b[:] for b in board]
  for loc in s:
    i, j = loc
    temp[i][j] = 0
  return temp

def gravity(m, n, board):
  cnt = 0
  for i in range(m-1):
    for j in range(n):
      if board[i][j] and board[i+1][j] == 0:
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        cnt += 1
  return cnt, board
            
def solution(m, n, board):
  answer = 0
  board = [list(b) for b in board]
  while True:
    s = find_four(m, n, board)
    answer += len(s)
    board = pop_four(s, board)
    cnt = 1
    while cnt:
      cnt, board = gravity(m, n, board)
    if cnt == 0 and len(s) == 0:
      break
  return answer