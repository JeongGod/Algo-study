dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    m, n = len(board), len(board[0])
    
    def dfs(x, y, idx):
      if idx == len(word) - 1:
        return True
      temp = board[x][y]
      board[x][y] = ''
      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[idx + 1]:
          if dfs(nx, ny, idx + 1):
            return True
      board[x][y] = temp
      return False
              
    for i in range(m):
      for j in range(n):
        if board[i][j] == word[0]:
          if dfs(i, j, 0):
            return True
    return False