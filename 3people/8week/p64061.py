from collections import deque

def solution(board, moves):
  answer = 0
  moves = [m-1 for m in moves]
  st = deque([])    
  l = len(board)
  for m in moves:
    for i in range(l):
      if board[i][m] == 0:
        continue
      else:
        if len(st) == 0:
          st.append(board[i][m])
          board[i][m] = 0
          break
        else:
          top = st[-1]
          if top == board[i][m]:
            st.pop()
            answer += 2
          else:
            st.append(board[i][m])
          board[i][m] = 0
          break
  return answer