from collections import deque
import sys
from typing import Deque, List, Tuple

dx: List[int] = [-1, 1, 0, 0]
dy: List[int] = [0, 0, -1, 1]


def bfs() -> int:
    last_day: int = 0
    while tomato_que:
        x, y = tomato_que.popleft()

        for i in range(4):
            nx: int = x + dx[i]
            ny: int = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if graph[nx][ny] > 0 or graph[nx][ny] == -1:
                continue

            graph[nx][ny] = graph[x][y] + 1
            last_day = graph[nx][ny]
            tomato_que.append((nx, ny))

    return 1 if last_day == 0 else last_day


if __name__ == "__main__":
    input = sys.stdin.readline
    M, N = map(int, input().split())
    graph: List[List[int]] = [
        list(map(int, input().split())) for _ in range(N)]
    tomato_que: Deque[Tuple[int, int]] = deque()
    is_possible: bool = True

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                tomato_que.append((i, j))

    answer: int = bfs()

    for row in graph:
        if 0 in row:
            is_possible = False
            break

    if is_possible:
        print(answer - 1)
    else:
        print(-1)
