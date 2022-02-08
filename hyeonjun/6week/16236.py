import sys
from collections import deque
input = sys.stdin.readline


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def choose_fish(fish_list):
    fish_list.sort()
    return fish_list[0][0], fish_list[0][1]


def bfs(start_x, start_y, shark_size, time):
    queue = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    can_eat = []
    flag = float('inf')

    queue.append((start_x, start_y, 0))
    board[start_x][start_y] = 0
    visited[start_x][start_y] = 1

    while queue:
        x, y, dist = queue.popleft()
        if dist+1 > flag:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if board[nx][ny] > shark_size[0]:
                    continue

                if not board[nx][ny] or board[nx][ny] == shark_size[0]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, dist+1))

                else:
                    flag = dist+1
                    visited[nx][ny] = 1
                    can_eat.append((nx, ny))

    if can_eat:
        next_x, next_y = choose_fish(can_eat)
        if shark_size[1]+1 == shark_size[0]:
            shark_size = [shark_size[0]+1, 0]
        else:
            shark_size[1] += 1
        bfs(next_x, next_y, shark_size, time+flag)

    else:
        print(time)

    return 0


def search_shark():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                return i, j


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    x, y = search_shark()
    bfs(x, y, [2, 0], 0)
