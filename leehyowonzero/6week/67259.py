from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solution(board):
    n = len(board)
    answer = float('inf')
    visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    visited[0][1][0] = 100 # (x, y, d) : cost
    visited[1][0][1] = 100
    q = deque()
    if(board[0][1] != 1):
        q.append((0, 1, 0, 100)) # 시작지점 기준 우측
    if(board[1][0] != 1):
        q.append((1, 0, 1, 100)) # 시작지점 기준 아래
    
    while q:
        x, y, dir, cost = q.popleft()
        if(x == n-1 and y == n-1):
            answer = min(answer, cost)
            continue
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if(board[nx][ny] == 1):
                continue
            if(dir == d): # 방향이 같음
                expense = 100
            elif(dir%2 == d%2): # 후진 거르기
                continue
            else: # 커브 생김
                expense = 600 
                
            if(visited[nx][ny][d] == 0): # 방문기록이 없으면
                visited[nx][ny][d] = cost + expense
                q.append([nx, ny, d, cost + expense])
            else:
                if(visited[nx][ny][d] > cost + expense):
                    visited[nx][ny][d] = cost + expense
                    q.append([nx, ny, d, cost + expense])
    return answer