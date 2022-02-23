import sys
input = sys.stdin.readline

dx = [0, -1, 0, 1] * 2
dy = [-1, 0, 1, 0] * 2


def find(x, y, d, cnt):
    board[x][y] = 2
    while True:
        for i in range(d, d-4, -1):
            empty = 0
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not board[nx][ny]:
                empty = 1
                break

        if empty:
            return find(nx, ny, (i+3) % 4, cnt + 1)

        else:
            x += dx[d-1]
            y += dy[d-1]
            if board[x][y] == 1:
                return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    print(find(r, c, d, 1))
