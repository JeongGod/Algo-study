from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def melt(length):
    arr = []
    for i in range(length):
        for j in range(length):
            if field[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < length and 0 <= ny < length and field[nx][ny] != 0:
                        cnt += 1
                if cnt < 3:
                    arr.append([i, j])
    for i in arr:
        field[i[0]][i[1]] -= 1


def count(length):
    rest = 0
    max_ice = 0
    queue = deque()
    for i in range(length):
        for j in range(length):
            if field[i][j] > 0:
                queue.append([i, j])
                rest += field[i][j]
                field[i][j] = -1
                tmp = -2
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < length and 0 <= ny < length and field[nx][ny] > 0:
                            rest += field[nx][ny]
                            field[nx][ny] = tmp
                            queue.append([nx, ny])
                            tmp -= 1
                max_ice = min(max_ice, tmp+1)
    print(rest)
    if max_ice != 0:
        print(-1*max_ice)
    else:
        print(0)


def rotate_90(cor, length):
    x, y = cor[0], cor[1]
    arr = []
    for i in range(length):
        arr.append(field[x+i][y:length+y])
    tmp = list(zip(*arr[::-1]))
    for i in range(length):
        field[x+i][y:length+y] = list(tmp)[i]


N, Q = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(2**N)]
order_L = list(map(int, input().split()))

for i in order_L:
    start = [0, 0]
    square = 2**i
    for j in range((2**N)**2//square**2):
        rotate_90(start, square)
        start[1] += square
        if start[1] >= 2**N:
            start[1] = 0
            start[0] += square
    melt(2**N)
count(2**N)
