import sys
input = sys.stdin.readline

move = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
dice = [0, 0, 0, 0, 0, 0]  # 위 남쪽 아래 북쪽 서쪽 동쪽

if __name__ == "__main__":
    n, m, x, y, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    orders = list(map(int, input().split()))

    for order in orders:
        dx, dy = move[order]
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if order == 1:
                dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]
            elif order == 2:
                dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]
            elif order == 3:
                dice[:3], dice[3] = dice[1:4], dice[0]
            else:
                dice[1:4], dice[0] = dice[:3], dice[3]

            if board[nx][ny]:
                dice[2] = board[nx][ny]
                board[nx][ny] = 0
            else:
                board[nx][ny] = dice[2]

            print(dice[0])

            x, y = nx, ny
