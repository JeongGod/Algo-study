from collections import deque


class Solution:
    
    
    def check(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    def bfs(self, x, y, grid):
        dq = deque([(x, y)])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        grid[x][y] = "0"
        while dq:
            cx, cy = dq.popleft()
            for gx, gy in zip(dx, dy):
                nx, ny = cx + gx, cy + gy
                
                if not self.check(nx, ny, grid) or grid[nx][ny] == "0":
                    continue
                
                grid[nx][ny] = "0"
                dq.append((nx, ny))
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        answer = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "0":
                    continue
                answer += 1
                self.bfs(x, y, grid)

        return answer
