import sys
from typing import List
sys.setrecursionlimit(10**4)

dx: List[int] = [0, 0, -1, 1]
dy: List[int] = [-1, 1, 0, 0]


def dfs(r, c) -> int:
    visited[r][c] = True
    result: int = 1
    for i in range(4):
        nr: int = r + dy[i]
        nc: int = c + dx[i]
        if (nr >= 0 and nc >= 0 and
            nr < N and nc < N and
                not visited[nr][nc] and graph[nr][nc] > 0):
            result += dfs(nr, nc)

    return result


def get_biggest() -> int:
    total: int = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0 and not visited[i][j]:
                total = max(total, dfs(i, j))
    return total


def get_ice_sum() -> int:
    total: int = 0
    for i in range(N):
        for j in range(N):
            total += graph[i][j]

    return total


def rotate(r: int, c: int, level: int) -> None:
    for i in range(level):
        for j in range(level):
            temp[i][j] = graph[r+level-1-j][c+i]

    for i in range(level):
        for j in range(level):
            graph[r+i][c+j] = temp[i][j]


if __name__ == "__main__":
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    N = 2**N
    temp: List[List[int]] = [[0] * (N) for _ in range(N)]
    graph: List[List[int]] = [list(map(int, input().split())) for _ in range(N)]
    L: List[int] = list(map(int, input().split()))

    for level in L:
        # 격자 회전
        visited = [[False] * (N) for _ in range(N)]
        melt_check = [[False] * (N) for _ in range(N)]
        for i in range(0, N, 2**level):
            for j in range(0, N, 2**level):
                rotate(i, j, 2**level)

        # 얼음 융해
        for i in range(N):
            for j in range(N):
                cnt: int = 0
                if graph[i][j] == 0:
                    continue

                for k in range(4):
                    ny: int = i + dy[k]
                    nx: int = j + dx[k]
                    if not (ny >= 0 and nx >= 0 and ny < N and nx < N):
                        continue

                    if graph[ny][nx] > 0:
                        cnt += 1

                if cnt < 3:
                    melt_check[i][j] = True

        for i in range(N):
            for j in range(N):
                if melt_check[i][j]:
                    graph[i][j] -= 1

    print(get_ice_sum())
    print(get_biggest())
