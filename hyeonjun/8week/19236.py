import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]*2
dy = [0, -1, -1, -1, 0, 1, 1, 1]*2


def simulation(copy_bowl, copy_shark, order, res):
    copy_order = move_fish(copy_bowl, copy_shark, order)
    move_shark(copy_bowl, copy_shark, copy_order, res)


def move_fish(copy_bowl, copy_shark, order):
    copy_order = copy.deepcopy(order)
    copy_order[copy_shark[2]-1][0] = -1
    for i in copy_order:
        if i[0] != -1:
            tmp = copy_bowl[i[0]][i[1]]
            for j in range(-1, 7):
                nx = i[0] + dx[tmp[1]+j]
                ny = i[1] + dy[tmp[1]+j]
                # 0: 상어, -1: 공란
                if 0 <= nx < 4 and 0 <= ny < 4 and copy_bowl[nx][ny][0] != 0:
                    if copy_bowl[nx][ny][0] == -1:
                        copy_order[tmp[0]-1] = [nx, ny]
                    else:
                        copy_order[tmp[0]-1], copy_order[copy_bowl[nx]
                                                         [ny][0]-1] = [nx, ny], i
                    copy_bowl[i[0]][i[1]][1] = (tmp[1]+j+1) % 8
                    copy_bowl[i[0]][i[1]
                                    ], copy_bowl[nx][ny] = copy_bowl[nx][ny], copy_bowl[i[0]][i[1]]
                    break
    return copy_order


def move_shark(copy_bowl, shark, copy_order, res):
    tmp = copy_bowl[shark[0]][shark[1]][1]
    flag = False
    for i in range(1, 4):
        nx = shark[0] + dx[tmp-1]*i
        ny = shark[1] + dy[tmp-1]*i
        if 0 <= nx < 4 and 0 <= ny < 4 and copy_bowl[nx][ny][0] != -1:
            flag = True
            copy_bowl2 = copy.deepcopy(copy_bowl)
            copy_bowl2[shark[0]][shark[1]] = [-1, -1]
            n_res = copy_bowl2[nx][ny][0] + res
            copy_shark = [nx, ny, copy_bowl2[nx][ny][0]]
            copy_bowl2[nx][ny][0] = 0
            simulation(copy_bowl2, copy_shark, copy_order, n_res)
    if flag == False:
        answer.append(res)


answer = []
bowl = [[[0, 0] for _ in range(4)] for _ in range(4)]
for i in range(4):
    bowl[i][0][0], bowl[i][0][1], bowl[i][1][0], bowl[i][1][1], bowl[i][2][0], bowl[i][2][1], bowl[i][3][0], bowl[i][3][1] = map(
        int, input().split())
res, bowl[0][0][0], shark = bowl[0][0][0], 0, [0, 0, bowl[0][0][0]]
order = [[0, 0] for _ in range(16)]  # 물고기 이동 순서
for i in range(4):
    for j in range(4):
        order[bowl[i][j][0]-1] = [i, j]
order[res-1][0] = -1
simulation(bowl, shark, order, res)
print(max(answer))
