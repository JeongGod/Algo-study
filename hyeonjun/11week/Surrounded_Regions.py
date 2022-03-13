from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        def check_flip(start_x, start_y):
            queue = deque()
            visited = [[0 for _ in range(n)] for _ in range(m)]
            queue.append((start_x, start_y))
            must_flip = [(start_x, start_y)]
            while queue:
                x, y = queue.pop()
                visited[x][y] = 1
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n:
                        if board[nx][ny] == 'O' and not visited[nx][ny]:
                            queue.append((nx, ny))
                            must_flip.append((nx, ny))
                    else:
                        return []
            return must_flip

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    for x, y in check_flip(i, j):
                        board[x][y] = 'X'
