import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def down(cand, cand_cnt, ground):
    while len(cand_cnt) != len(ground):
        for cluster in cand_cnt:
            if cluster not in ground:
                for x, y in cand[cluster]:
                    cave[x][y] = '.'
                for i in range(len(cand[cluster])):
                    x, y = cand[cluster][i]
                    cave[x+1][y] = cluster
                    cand[cluster][i][0] += 1
            else:
                for x, y in cand[cluster]:
                    cave[x][y] = 'x'
        for cluster in cand_cnt:
            if cluster not in ground:
                for x, y in cand[cluster]:
                    if x+1 == R or cave[x+1][y] == 'x':
                        ground.add(cluster)
                        break
    for i in range(R):
        for j in range(C):
            if cave[i][j] != '.' and cave[i][j] != 'x':
                cave[i][j] = 'x'


def dfs(mineral_x, mineral_y):
    stack = []
    stack.append([mineral_x, mineral_y])
    cave[mineral_x][mineral_y] = '.'
    cluster_num = 0
    cand = [[] for _ in range(4)]
    cand_cnt = []
    cluster_ground = set()
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if x == mineral_x and y == mineral_y:
                if 0 <= nx < R and 0 <= ny < C and cave[nx][ny] != '.':
                    cave[nx][ny] = cluster_num
                    cand[cluster_num].append([nx, ny])
                    cand_cnt.append(cluster_num)
                    stack.append([nx, ny])
                cluster_num += 1
            else:
                if 0 <= nx < R and 0 <= ny < C and cave[nx][ny] != '.' and cave[nx][ny] != cave[x][y]:
                    if cave[nx][ny] != 'x':
                        cand_cnt.remove(cave[nx][ny])
                    cave[nx][ny] = cave[x][y]
                    cand[cave[x][y]].append([nx, ny])
                    stack.append([nx, ny])
                    if nx+1 == R:
                        cluster_ground.add(cave[nx][ny])
    down(cand, cand_cnt, cluster_ground)


def check_mineral(x, left):
    if left:
        a, b, c = 0, C, 1
    else:
        a, b, c = C-1, -1, -1
    for i in range(a, b, c):
        if cave[x][i] != '.':
            return (x, i)
    return (-1, -1)


R, C = map(int, input().split())
cave = [list(str(input().rstrip())) for _ in range(R)]
N = int(input())
height = list(map(int, input().split()))

left = True
for i in height:
    x, y = check_mineral(R-i, left)
    left = not left
    if x != -1:
        dfs(x, y)

for i in cave:
    print(''.join(i))
