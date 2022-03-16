from collections import deque


class Solution:
    
    
    def solve(self, board : List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        def check(x : int, y : int):
            return 0 <= x < n and 0 <= y < m
        
        def bfs(x : int, y : int) -> None:
            dq = deque([(x, y)])
            visited[x][y] = True
            a = [(x, y)]
            flag = True
            while dq:
                cx, cy = dq.popleft()
                if not (0 < cx < n-1 and 0 < cy < m-1):
                    flag = False
                for gx, gy in zip(dx, dy):
                    nx, ny = cx + gx, cy + gy
                    if not check(nx, ny):
                        continue
                    # 벽에 붙어있다면
                    if visited[nx][ny]:
                        continue
                    if board[nx][ny] == "X":
                        continue
                    visited[nx][ny] = True
                    dq.append((nx, ny))
                    a.append((nx, ny))
            if not flag:
                return
            # flip
            for i, j in a:
                board[i][j] = "X"
        
        
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "X":
                    continue
                if visited[i][j]:
                    continue
                bfs(i, j)
