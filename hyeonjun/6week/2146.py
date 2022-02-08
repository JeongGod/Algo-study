import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def make_bridge(continents):
    minimum_dist = float('inf')
    for idx, start_continent in enumerate(continents):
        for end_continent in continents[idx+1:]:
            for start_x, start_y in start_continent:
                for end_x, end_y in end_continent:
                    minimum_dist = min(minimum_dist, abs(
                        start_x-end_x)+abs(start_y-end_y)-1)
    print(minimum_dist)
    return 0


def bfs(start_x, start_y):
    continent = set()
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not board[nx][ny]:
                    continent.add((x, y))
                elif board[nx][ny] == 1:
                    board[nx][ny] = -1
                    queue.append((nx, ny))
    return continent


def classify_continent():
    continents = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                continents.append(bfs(i, j))
    return continents


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    make_bridge(classify_continent())
