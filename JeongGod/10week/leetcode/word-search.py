dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        global row, col
        row, col = len(board), len(board[0])
        
        for x in range(row):
            for y in range(col):
                if board[x][y] == word[0]:
                    if self.dfs(board, word, x, y, 1):
                        return True
        return False
    
    def dfs(self, board, word, x, y, idx):
        if idx == len(word):
            return True
        tmp = board[x][y]
        board[x][y] = "#"
        for gx, gy in zip(dx, dy):
            nx, ny = x + gx, y + gy
                
            if not (0 <= nx < row and 0 <= ny < col):
                continue
            if board[nx][ny] != word[idx]:
                continue
            result = self.dfs(board, word, nx, ny, idx+1)
            if result:
                return result
        board[x][y] = tmp
        return False
