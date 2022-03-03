dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search_start(target):
            cands = []
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell == target:
                        cands.append([i, j])
            return cands

        def dfs(x, y, target_idx):
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == word[target_idx]:
                    if target_idx == len(word)-1 or dfs(nx, ny, target_idx+1):
                        return True
                    visited[nx][ny] = 0
            return False

        N, M = len(board), len(board[0])
        cands = search_start(word[0])

        if len(word) == 1 and cands:
            return True

        visited = [[0 for _ in range(M)] for _ in range(N)]
        for x, y in cands:
            if dfs(x, y, 1):
                return True
            visited[x][y] = 0
        return False
