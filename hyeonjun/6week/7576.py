import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def bfs(tomatoes):
    global unripe_tomato
    queue = deque()
    time = 0
    for x, y in tomatoes:
        box[x][y] = -1
        queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        time = box[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not box[nx][ny]:
                box[nx][ny] = time-1
                unripe_tomato -= 1
                queue.append((nx, ny))

    if unripe_tomato:
        print(-1)
    else:
        print(abs(time+1))


def check_tomato():
    global unripe_tomato
    ripe_tomato = []
    flag = False
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                ripe_tomato.append((i, j))
            elif box[i][j] == 0:
                unripe_tomato += 1
                flag = True
    if flag:
        if ripe_tomato:
            return ripe_tomato
        else:
            print(-1)
            return 0
    else:
        print(0)
        return 0


if __name__ == "__main__":
    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    unripe_tomato = 0
    ripe_tomato = check_tomato()
    if ripe_tomato:
        bfs(ripe_tomato)
