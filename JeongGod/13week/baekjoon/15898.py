"""
1. 5*5 격자 모양에 서로 다른 재료 3개를 넣는다.
2. 넣을 수 있는 재료의 후보는 10개 이하이다.
3. 주어진 재료중 3개를 선택해 순서를 정해 가마에 넣어야 한다.

재료는 4*4모양으로 생겼다.
재료는 회전해서 넣을 수 있다.

재료의 원소가 흰색 => 그대로 간다.
아니라면 원소와 같은 색으로 칠해진다.

폭탄의 품질 = 7R + 5B + 3G + 2Y
"""
import sys
from itertools import permutations

input = sys.stdin.readline

def insert_board(picks : list[tuple[list[list[int]], list[list[str]]]], pos : list[tuple[int, int]]) -> list[list[int]]:
    score_board = [[0] * 5 for _ in range(5)]
    color_board = [["W"] * 5 for _ in range(5)]
    # gx -> gy -> gz순으로 넣는다.
    for idx in range(3):
        score_cur = picks[idx][0]
        color_cur = picks[idx][1]
        sx, sy = pos[idx]
        for i in range(4):
            for j in range(4):
                score_board[sx+i][sy+j] += score_cur[i][j]
                if score_board[sx+i][sy+j] > 9:
                    score_board[sx+i][sy+j] = 9
                elif score_board[sx+i][sy+j] < 0:
                    score_board[sx+i][sy+j] = 0
                if color_cur[i][j] == "W":
                    continue
                color_board[sx+i][sy+j] = color_cur[i][j]
    
    return score_board, color_board

def calc(sboard : list[list[int]], cboard : list[list[str]]) -> int:
    result = 0
    for i in range(5):
        for j in range(5):
            if cboard[i][j] == "R":
                result += (7 * sboard[i][j])
            elif cboard[i][j] == "B":
                result += (5 * sboard[i][j])
            elif cboard[i][j] == "G":
                result += (3 * sboard[i][j])
            elif cboard[i][j] == "Y":
                result += (2 * sboard[i][j])
    return result

def rotate(q : list[list[int]], c : list[list[int]]) -> tuple[list[list[int]], list[list[str]]]:
    nq, nc = [], []
    def make_arr(arr, target):
        for j in range(4):
            tmp = []
            for i in range(3, -1, -1):
                tmp.append(target[i][j])
            arr.append(tmp)
    make_arr(nq, q), make_arr(nc, c)
    return nq, nc

def solution(n : int, ingredient : dict):
    orders = []
    position = [(0, 0), (0, 1), (1, 0), (1, 1)]
    answer = 0
    # 재료를 선택한다.
    for per in permutations(range(n), 3):
        orders.append(per)
    # 해당 재료들을 넣는다.
    for x, y, z in orders:
        # 어떠한 회전 재료를 담을지 뽑는다.
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    picks = [ingredient[x][i], ingredient[y][j], ingredient[z][k]]
                    # 어느 지점에다가 재료를 넣을지 선택한다.
                    for sx in range(4):
                        for sy in range(4):
                            for sz in range(4):
                                picks_pos = [position[sx], position[sy], position[sz]]
                                sboard, cboard = insert_board(picks, picks_pos)
                                answer = max(answer, calc(sboard, cboard))

        # insert_board[gradient[x][0], gradient[y][0], gradient[z][0]]
    return answer

if __name__ == "__main__":
    N = int(input())
    ingredient = dict()
    for i in range(N):
        quality = []
        for _ in range(4):
            quality.append(list(map(int, input().split())))
        color = []
        for _ in range(4):
            color.append(list(input().rstrip().split()))
        # 시계방향으로 회전시켜서 같이 넣어놓는다.
        ingredient[i] = [(quality, color)]
        for _ in range(3):
            quality, color = rotate(quality, color)
            ingredient[i].append((quality, color))
        
    print(solution(N, ingredient))
