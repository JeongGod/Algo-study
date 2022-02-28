dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
# 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.

N, M = map(int, input().split())
robotpos = list(map(int, input().split()))
Map = []
for _ in range(N):
    Map.append(list(map(int, input().split())))

cleaned = [[False for _ in range(M)] for _ in range(N)]
answer = 0
while True:
    x = robotpos[0]
    y = robotpos[1]
    dir = robotpos[2]
    # 현재 위치를 청소한다.
    if(cleaned[x][y] == False):
        cleaned[x][y] = True
        answer += 1
    # 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
    # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    flag = True
    for d in range(1, 5):
        nx = x + dx[(dir - d)%4]
        ny = y + dy[(dir - d)%4]
        if not (0 <= nx < N and 0 <= ny < M): # 범위 벗어남
            continue
        if(Map[nx][ny] == 1): # 벽
            continue
        if(cleaned[nx][ny] == False):
            robotpos = [nx, ny, (dir - d)%4]
            flag = False
            break
    if(flag):
        robotpos = [robotpos[0]-dx[robotpos[2]], robotpos[1]-dy[robotpos[2]], robotpos[2]]
        if(Map[robotpos[0]][robotpos[1]] == 1):
            break

print(answer)