import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

hx = [1, 2, 1, 2, -1, -2, -1, -2]
hy = [2, 1, -2, -1, 2, 1, -2, -1]


def check(x: int, y: int, board: list[list[int]]) -> bool:
    return (0 <= x < H and 0 <= y < W) and board[x][y] == 0


def solution(k: int, board: list[list[int]]) -> int:
    dq = deque([(0, 0, 0, 0)])
    visited = [[[False] * (k + 1) for _ in range(W)] for _ in range(H)]

    for i in range(k):
        visited[0][0][i] = True

    while dq:
        cx, cy, cnt, ck = dq.popleft()
        if cx == H - 1 and cy == W - 1:
            return cnt
        if ck < k:
            for gx, gy in zip(hx, hy):
                nx, ny = cx + gx, cy + gy
                if not check(nx, ny, board) or visited[nx][ny][ck + 1]:
                    continue
                visited[nx][ny][ck + 1] = True
                dq.append((nx, ny, cnt + 1, ck + 1))

        for gx, gy in zip(dx, dy):
            nx, ny = cx + gx, cy + gy
            if not check(nx, ny, board) or visited[nx][ny][ck]:
                continue
            visited[nx][ny][ck] = True
            dq.append((nx, ny, cnt + 1, ck))

    return -1


if __name__ == "__main__":
    K = int(input())
    W, H = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(H)]
    print(solution(K, board))
