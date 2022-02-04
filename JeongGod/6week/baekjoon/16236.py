import sys
from collections import deque
from typing import List, Tuple

input = sys.stdin.readline
"""
아기 상어 크기 = 2
상하좌우로 한 칸씩 이동
아기 상어 > 물고기 => 이동 가능 => 같으면 이동만 가능
아기 상어 < 물고기 => 이동 불가

자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1증가한다.
"""
MAX_DIST = 401

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def check(x : int, y : int) -> bool:
    if not (0 <= x < N and 0 <= y < N):
        return False
    if baby_shark_size < board[x][y]:
        return False
    return True

def find_fish(x : int, y : int) -> List[int]:
    dq = deque([(x, y, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    go = False
    target_cnt = 1e9
    possible = []
    while dq:
        cx, cy, cnt = dq.popleft()
        if board[cx][cy] != 0 and board[cx][cy] < baby_shark_size and cnt <= target_cnt:
            possible.append((cx, cy, cnt))
            target_cnt = cnt
            go = True
        if go:
            continue
        for gx, gy in zip(dx, dy):
            nx, ny = cx + gx, cy + gy
            if not check(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            dq.append((nx, ny, cnt+1))

    return min(possible, key=lambda x: (x[0], x[1])) if possible else [-1, -1, -1]

def solution(baby_shark : List[int]):
    global baby_shark_size
    """
    1. 가장 작은 물고기의 위치를 알아낸다.
    2. 해당 위치로 이동한다.
    3. 1번부터 다시 시작한다.
    """
    answer = 0
    cnt = 0
    while True:
        fish_x, fish_y, fish_dist = find_fish(baby_shark[0], baby_shark[1])
        if fish_dist == -1:
            break
        # 해당 물고기는 먹는다.
        board[fish_x][fish_y] = 0
        cnt += 1
        # 상어가 커지는지
        if cnt == baby_shark_size:
            baby_shark_size += 1
            cnt = 0
        # 거리를 잰다.
        answer += fish_dist
        # 상어 위치 이동
        baby_shark = [fish_x, fish_y]

    return answer

if __name__ == "__main__":
    N = int(input())
    board = []
    baby_shark = [0, 0]
    baby_shark_size = 2
    for i in range(N):
        tmp = list(map(int, input().split()))
        board.append(tmp)
        # 물고기와 아기상어의 위치
        for j in range(N):
            if tmp[j] == 9:
                baby_shark = [i, j]
                board[i][j] = 0
    print(solution(baby_shark))
