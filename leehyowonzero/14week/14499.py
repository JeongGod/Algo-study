# 주사위를 굴리는게 아닌 주사위는 그냥 옮기고 위에 있는 숫자를 돌려준다고 생각
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
# 기본 입력 받기
n, m, x, y, k = map(int,input().split())
Map = []
for _ in range(n):
    Map.append(list(map(int,input().split())))
    
command = list(map(int,input().split()))

dice = [0,0,0,0,0,0] #dice[0] 바닥 dice[5] 천장
dice[0] = Map[x][y]
for d in command:
    nx = x + dx[d]
    ny = y + dy[d]
    if not (0 <= nx < n and 0 <= ny < m):
        continue
    x = nx
    y = ny
    if(d == 1):
        dice[0],dice[2],dice[3],dice[5] = dice[2],dice[5],dice[0],dice[3]
    elif(d == 2):
        dice[0],dice[2],dice[3],dice[5] = dice[3],dice[0],dice[5],dice[2]
    elif(d == 3):
        dice[0],dice[1],dice[4],dice[5] = dice[1],dice[5],dice[0],dice[4]
    elif(d == 4):
        dice[0],dice[1],dice[4],dice[5] = dice[4],dice[0],dice[5],dice[1]
        
    if(Map[nx][ny] == 0):
        Map[nx][ny] = dice[0]
    else:
        dice[0] = Map[nx][ny]
        Map[nx][ny] = 0
    print(dice[5])