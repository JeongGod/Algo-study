import sys
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
horse_dx = [1,1,2,2,-1,-1,-2,-2]
horse_dy = [2,-2,1,-1,2,-2,1,-1]
MAXSIZE = sys.maxsize

k = int(input())
w, h = map(int,input().split())
Map = []
for _ in range(h):
    Map.append(list(map(int,input().split())))

start = [0, 0]
dp = [[[MAXSIZE for _ in range(k+1)] for _ in range(w)] for _ in range(h)]
for i in range(k+1):
    
    dp[0][0][i] = 0

q = deque()
q.append([start, 0, 0]) # 좌표, 이동횟수 , 홀스무브 사용 횟수
while q:
    nowpos, move_cnt, horse_move_cnt = q.popleft()
    for d in range(4): # 기본이동
        nx = nowpos[0] + dx[d]
        ny = nowpos[1] + dy[d]
        if not ( 0 <= nx < h and 0 <= ny < w):
            continue
        if(Map[nx][ny] == 1):
            continue
        if(dp[nx][ny][horse_move_cnt] > move_cnt + 1):
            dp[nx][ny][horse_move_cnt] = move_cnt + 1
            q.append([[nx,ny], move_cnt + 1, horse_move_cnt])
    for d in range(8):
        if(horse_move_cnt == k):
            continue
        nx = nowpos[0] + horse_dx[d]
        ny = nowpos[1] + horse_dy[d]
        if not ( 0 <= nx < h and 0 <= ny < w):
            continue
        if(Map[nx][ny] == 1):
            continue
        if(dp[nx][ny][horse_move_cnt + 1] > move_cnt + 1):
            dp[nx][ny][horse_move_cnt + 1] = move_cnt + 1
            q.append([[nx,ny], move_cnt + 1, horse_move_cnt + 1])
answer = min(dp[h-1][w-1])
if(answer == MAXSIZE):
    print(-1)
else:
    print(answer)
        