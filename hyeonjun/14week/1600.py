import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

h_dx = [-1, -2, -2, -1, 1, 2, 2, 1]
h_dy = [-2, -2, 1, 2, 2, 1, -1, -2]


def can_go(x, y, horse_move):
    if 0 <= x < H and 0 <= y < W and board[x][y] != 1 and visited[x][y] < horse_move:
        return True
    return False


def move(start_x, start_y, horse_move):
    queue = deque()
    queue.append((start_x, start_y, horse_move, -1))
    while queue:
        x, y, remain_horse, cnt = queue.popleft()
        if x == H-1 and y == W-1:
            return -(cnt+1)

        if remain_horse:
            for i in range(8):
                nx = x + h_dx[i]
                ny = y + h_dy[i]
                if can_go(nx, ny, remain_horse-1):
                    board[nx][ny] = cnt
                    visited[nx][ny] = remain_horse-1
                    queue.append((nx, ny, remain_horse-1, cnt-1))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if can_go(nx, ny, remain_horse):
                board[nx][ny] = cnt
                visited[nx][ny] = remain_horse
                queue.append((nx, ny, remain_horse, cnt-1))

    return -1


if __name__ == "__main__":
    K = int(input())
    W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    visited = [[-1 for _ in range(W)] for _ in range(H)]
    board[0][0] = 1
    visited[0][0] = K
    print(move(0, 0, K))
