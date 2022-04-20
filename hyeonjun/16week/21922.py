import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def search_ac():
    ac = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 9:
                ac.append((i, j))
    return ac


def move_wind(ac):
    visited = [[[0, 0, 0, 0] for _ in range(M)] for _ in range(N)]
    for ac_x, ac_y in ac:
        board[ac_x][ac_y] = -5
        visited[ac_x][ac_y] = [1, 1, 1, 1]
        for i in range(4):
            nx, ny = ac_x, ac_y
            move_x, move_y = dx[i], dy[i]
            check = i
            while True:
                nx += move_x
                ny += move_y
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][check]:
                    visited[nx][ny][check] = 1
                    if not board[nx][ny]:
                        board[nx][ny] = -5
                        visited[nx][ny][check] = 1
                        continue
                    # if visited[nx][ny][check]:
                    #     continue
                    # else:

                    if board[nx][ny] > 0:
                        board[nx][ny] *= -1
                    if move_x and abs(board[nx][ny]) == 2:
                        break
                    elif move_y and abs(board[nx][ny]) == 1:
                        break
                    elif abs(board[nx][ny]) == 3:
                        if move_x:
                            if move_x == 1:
                                move_y = -1
                                check = 0
                            else:
                                move_y = 1
                                check = 1
                            move_x = 0
                        elif move_y:
                            if move_y == 1:
                                move_x = -1
                                check = 3
                            else:
                                move_x = 1
                                check = 2
                            move_y = 0
                        visited[nx][ny][check] = 1
                    elif abs(board[nx][ny]) == 4:
                        if move_x:
                            if move_x == 1:
                                move_y = 1
                                check = 1
                            else:
                                move_y = -1
                                check = 0
                            move_x = 0
                        elif move_y:
                            if move_y == 1:
                                move_x = 1
                                check = 2
                            else:
                                move_x = -1
                                check = 3
                            move_y = 0
                        visited[nx][ny][check] = 1
                else:
                    break


def calc():
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] < 0:
                answer += 1
    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ac = search_ac()
    move_wind(ac)
    print(calc())
