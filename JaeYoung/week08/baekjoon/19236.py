# 아이디어 -> dfs를 사용해 이동경로에 대한 최대값을 구함
import sys
from copy import deepcopy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(x, y, shark, cnt) -> None:
    global answer, Map, fish
    move_fish(x, y)
    while True:
        nx, ny = x + dx[shark], y + dy[shark]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            answer = max(answer, cnt)
            return
        if not Map[nx][ny]:
            x, y = nx, ny
            continue

        temp_a, temp_fish = deepcopy(Map), deepcopy(fish)
        temp1, temp2 = fish[Map[nx][ny][0]], Map[nx][ny]
        fish[Map[nx][ny][0]], Map[nx][ny] = [], []
        dfs(nx, ny, temp2[1], cnt + temp2[0] + 1)
        Map, fish = temp_a, temp_fish
        fish[Map[nx][ny][0]], Map[nx][ny] = temp1, temp2
        x, y = nx, ny


def move_fish(ax, ay) -> None:
    for i in range(16):
        if fish[i]:
            x, y = fish[i][0], fish[i][1]
            for _ in range(9):
                nx, ny = x + dx[Map[x][y][1]], y + dy[Map[x][y][1]]
                if not 0 <= nx < 4 or not 0 <= ny < 4 or (nx == ax and ny == ay):
                    Map[x][y][1] = (Map[x][y][1] + 1) % 8
                    continue
                if Map[nx][ny]:
                    fish[Map[nx][ny][0]] = [x, y]
                Map[nx][ny], Map[x][y] = Map[x][y], Map[nx][ny]
                fish[i] = [nx, ny]
                break

if __name__ == "__main__":
    input = sys.stdin.readline
    Map = [[] for _ in range(4)]
    fish = [[] for _ in range(16)]
    for i in range(4):
        temp = list(map(int, input().split()))
        for j in range(0, 7, 2):
            Map[i].append([temp[j]-1, temp[j+1]-1])
            fish[temp[j]-1] = [i, j // 2]

    answer = 0
    shark, cnt = Map[0][0][1], Map[0][0][0] + 1
    fish[Map[0][0][0]], Map[0][0] = [], []
    dfs(0, 0, shark, cnt)
    print(answer)
