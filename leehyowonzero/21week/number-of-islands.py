from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y , grid):
    q = deque()
    q.append([x,y])
    while q :
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not(0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                continue
            if(grid[nx][ny] == "1"):
                grid[nx][ny] = "0"
                q.append([nx, ny])
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1"):
                    bfs(i, j, grid)
                    answer += 1
                    
                    
        return answer