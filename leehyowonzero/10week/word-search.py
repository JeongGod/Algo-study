class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [0, 0, 1 ,-1]
        dy = [1, -1, 0, 0]

        def dfs(x, y, idx):
            if(idx == len(word)-1):
                return True
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
                    continue
                if(visited[nx][ny] == True):
                    continue
                if(board[nx][ny] == word[idx+1]):
                    visited[nx][ny] = True
                    if(dfs(nx, ny, idx+1)):
                        return True
                    visited[nx][ny] = False
                    
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == word[0]):
                    visited[i][j] = True
                    if(dfs(i, j, 0)):
                        return True
                    visited[i][j] = False
        return False