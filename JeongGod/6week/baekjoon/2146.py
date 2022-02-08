import sys
from collections import deque
from typing import Set, Tuple

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def check(x : int, y : int) -> bool:
    if not(0 <= x < N and 0 <= y < N):
        return False
    return True

def find_island(x : int, y : int) -> Set[Tuple[int, int]]:
    dq = deque([(x, y)])
    island = {(x, y, 0)}

    while dq:
        cx, cy = dq.popleft()
        for gx, gy in zip(dx, dy):
            nx, ny = cx + gx, cy + gy
            if not check(nx, ny):
                continue
            # 섬이 아니거나, 이미 방문한 곳이라면
            if board[nx][ny] != -1 or (nx, ny, 0) in island:
                continue
            island.add((nx, ny, 0))
            dq.append((nx, ny))
    return island

def find_bridge(island : Set[Tuple[int, int]]) -> int:
    dq = deque(island)
    visited = [[200] * N for _ in range(N)]
    while dq:
        cx, cy, dist = dq.popleft()
        # 최소 다리를 찾았다면
        if board[cx][cy] == -1 and dist != 0:
            return dist - 1
        for gx, gy in zip(dx, dy):
            nx, ny = cx + gx, cy + gy
            if not check(nx, ny):
                continue
            # 같은 섬을 방문하는거면
            if (nx, ny, 0) in island:
                continue
            # 최소거리가 아니라면
            if visited[nx][ny] <= dist+1:
                continue
            visited[nx][ny] = dist+1
            dq.append((nx, ny, dist+1))
    return 1e9

def solution() -> int:
    """
    1. BFS로 탐색한다. 모든 육지의 점을 담는다.
    2. 상하좌우를 탐색한다. 만약 -1(육지)거나 현재 내가 있는 공간 >= 움직인 거리면 탐색한다.
    3. 그러다가 움직인 거리가 1이상이고 -1(육지)를 만나면 그만둔다.
    """
    answer = 1e9
    visited = set()
    for i in range(N):
        for j in range(N):
            # 섬이 아니거나 이미 방문한 섬이라면
            if board[i][j] != -1 or (i, j, 0) in visited:
                continue
            island = find_island(i, j)
            
            visited |= island
            # 해당 섬에서 다른 섬으로 가는 다리를 찾는다.
            dist = find_bridge(island)
            answer = min(dist, answer)

    return answer

if __name__ == "__main__":
    N = int(input())
    board = [list(map(lambda x: -int(x), input().split())) for _ in range(N)]
    
    print(solution())
