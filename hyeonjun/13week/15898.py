import sys
from itertools import permutations
from copy import deepcopy
input = sys.stdin.readline

color_to_cnt = {'R': 7, 'B': 5, 'G': 3, 'Y': 2, 'W': 0}


def calculate(target):
    global answer
    cnt = 0
    for i in range(5):
        for j in range(5):
            cnt += target[i][j][0]*target[i][j][1]
    answer = max(answer, cnt)
    return 0


def put(x, y, target, idx, kiln):
    copy_klin = deepcopy(kiln)
    for i in range(4):
        for j in range(4):
            add_num = copy_klin[x+i][y+j][0] + target[idx][i][j][0]
            copy_klin[x+i][y+j][0] = min(max(0, add_num), 9)
            if target[idx][i][j][1]:
                copy_klin[x+i][y+j][1] = target[idx][i][j][1]
    return copy_klin


def go(kiln, order, idx):
    if idx == 3:
        calculate(kiln)
        return 0

    cand_start = [(0, 0), (1, 0), (0, 1), (1, 1)]
    for i in range(4):
        x, y = cand_start[i]
        go(put(x, y, materials1, order[idx], kiln), order, idx+1)
        go(put(x, y, materials2, order[idx], kiln), order, idx+1)
        go(put(x, y, materials3, order[idx], kiln), order, idx+1)
        go(put(x, y, materials4, order[idx], kiln), order, idx+1)


def rotate(material):  # 90도 회전
    ret = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            ret[j][3-i] = material[i][j]
    return ret


if __name__ == '__main__':
    answer = 0
    n = int(input())
    kiln = [[[0, 0]for _ in range(5)] for _ in range(5)]
    materials1 = [[[[0, 0] for _ in range(4)] for _ in range(4)]
                  for _ in range(n)]
    materials2 = [[[[0, 0] for _ in range(4)] for _ in range(4)]
                  for _ in range(n)]
    materials3 = [[[[0, 0] for _ in range(4)] for _ in range(4)]
                  for _ in range(n)]
    materials4 = [[[[0, 0] for _ in range(4)] for _ in range(4)]
                  for _ in range(n)]
    for i in range(n):
        for j in range(4):
            nums = list(map(int, input().split()))
            for k, num in enumerate(nums):
                materials1[i][j][k][0] = num
        for j in range(4):
            colors = list(map(str, input().split()))
            for k, color in enumerate(colors):
                materials1[i][j][k][1] = color_to_cnt[color]
        materials2[i] = rotate(materials1[i])
        materials3[i] = rotate(materials2[i])
        materials4[i] = rotate(materials3[i])

    orders = permutations([i for i in range(n)], 3)
    for order in orders:
        go(kiln, order, 0)
    print(answer)
