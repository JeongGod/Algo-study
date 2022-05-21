class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]

        def search(x, y):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    search(nx, ny)
            return 0

        ans = 0
        m, n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    search(x, y)
                    ans += 1

        return ans
