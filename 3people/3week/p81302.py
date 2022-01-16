from collections import deque

def bfs(p):
  start = []
  for i in range(5):
    for j in range(5):
      if p[i][j] == 'P':
        start.append([i, j])
  for s in start:
    deq = deque([s])
    visited = [[0]*5 for _ in range(5)]
    dist = [[0]*5 for _ in range(5)]
    visited[s[0]][s[1]] = 1
    
    while deq:
      x, y = deq.popleft()
      dx = [-1, 1, 0, 0]
      dy = [0, 0, -1, 1]
      
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
          if p[nx][ny] == 'O':
            deq.append([nx, ny])
            visited[nx][ny] = 1
            dist[nx][ny] = dist[x][y] + 1
          if p[nx][ny] == 'P' and dist[x][y] <= 1:
            return 0
  return 1

def solution(places):
  answer = []
  for p in places:
    answer.append(bfs(p))
  return answer