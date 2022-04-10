# 주사위를 굴리는게 아닌 주사위는 그냥 옮기고 위에 있는 숫자를 돌려준다고 생각
from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def getscore(x, y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    ret = 1
    pivot = Map[x][y]
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if(visited[nx][ny]):
                continue
            if(Map[nx][ny] == pivot):
                visited[nx][ny] = True
                q.append([nx, ny])
                ret += 1
    # print("이번 이동으로 획득 점수")
    # print(pivot * ret)
    return pivot * ret
# 기본 입력 받기
n, m, k = map(int,input().split())
Map = []
for _ in range(n):
    Map.append(list(map(int,input().split())))
dice = [1,6,4,3,5,2] #dice[1] 바닥
x, y = [0, 0]
d = 0 
score = 0
for _ in range(k):
    nx = x + dx[d]
    ny = y + dy[d]
    if not (0 <= nx < n and 0 <= ny < m):
        nx = x - dx[d]
        ny = y - dy[d]
        d = (d+2)%4 # 방향전환
    x = nx
    y = ny
    if(d == 0):
        dice[0],dice[1],dice[2],dice[3] = dice[2],dice[3],dice[1],dice[0]
    elif(d == 1):
        dice[0],dice[1],dice[4],dice[5] = dice[5],dice[4],dice[0],dice[1]
    elif(d == 2):
        dice[0],dice[1],dice[2],dice[3] = dice[3],dice[2],dice[0],dice[1]
    elif(d == 3):
        dice[0],dice[1],dice[4],dice[5] = dice[4],dice[5],dice[1],dice[0]

    score += getscore(x, y)
    if(Map[x][y] < dice[1]):
        d = (d+1)%4
    elif(Map[x][y] > dice[1]):
        d = (d+3)%4
    # print("이동 후 주사위 전개도")    
    # print(dice)
    # print("이동 후 주사위 위치 및 결정된 이동방향")
    # print(x+1, y+1, d)
print(score)