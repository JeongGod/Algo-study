from collections import deque
import sys

R, C = map(int, sys.stdin.readline().split())
cave = [list(sys.stdin.readline().strip()) for _ in range(R)]
N = int(sys.stdin.readline().strip())
stick_heights = list(map(int, sys.stdin.readline().split()))
que = deque()
direction = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def stick_throw(x, direction):
    x, y = R-x, 0

    if direction == 1:
        for i in range(C):
            if cave[x][i] == 'x':
                cave[x][i] = '.'
                y = i
                break
    else:
        for i in range(C-1, -1, -1):
            if cave[x][i] == 'x':
                cave[x][i] = '.'
                y = i
                break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if cave[nx][ny] == 'x':
                que.append([nx, ny])


def bfs(x, y):
    bfs_que = deque()
    visited = [[0]*C for _ in range(R)]
    candidates = []
    bfs_que.append([x, y])
    visited[x][y] = 1
    while bfs_que:
        x, y = bfs_que.popleft()
        if x == R-1:
            return

        if cave[x+1][y] == '.':
            candidates.append([x, y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if cave[nx][ny] == 'x' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    bfs_que.append([nx, ny])

    cluster_down(visited, candidates)


def cluster_down(visited, candidates):
    k, flag = 1, 0

    while True:
        for i, j in candidates:
            if i + k == R-1:
                flag = 1
                break
            if cave[i+k+1][j] == "x" and not visited[i+k+1][j]:
                flag = 1
                break
        if flag:
            break
        k += 1

    for i in range(R-2, -1, -1):
        for j in range(C):
            if cave[i][j] == 'x' and visited[i][j]:
                cave[i][j] = '.'
                cave[i+k][j] = 'x'


while N:
    idx = stick_heights.pop(0)
    stick_throw(idx, direction)

    while que:
        x, y = que.popleft()
        bfs(x, y)

    direction *= -1
    N -= 1

for i in range(R):
    for j in range(C):
        print(cave[i][j], end='')
    print()
