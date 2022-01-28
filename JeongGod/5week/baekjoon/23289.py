# 3:20, 3:40, 4:42
import sys
from collections import deque
from typing import List, Set, Tuple

input = sys.stdin.readline
# (dx, dy)

RIGHT, LEFT, UP, DOWN = 1, 2, 3, 4
t = {LEFT : RIGHT, RIGHT : LEFT, UP : DOWN, DOWN : UP}
dist = {
    RIGHT : [(-1, 1, UP), (0, 1, RIGHT), (1, 1, DOWN)],
    LEFT : [(-1, -1, UP), (0, -1, LEFT), (1, -1, DOWN)],
    UP : [(-1, -1, LEFT), (-1, 0, UP), (-1, 1, RIGHT)],
    DOWN : [(1, -1, LEFT), (1, 0, DOWN), (1, 1, RIGHT)],
    }
def onair(warm_air : List[Tuple[int, int, int]], walls : Set[Tuple[int, int, int]]) -> None:
    """
    1. 바람이 먼저 양옆으로 빠지고 나서 방향으로 전진한다.
    2. 
    
    """
    def valid_check(x: int, y: int) -> bool:
        if 0 <= x < R and 0 <= y < C:
            return True
        return False

    for x, y, kind in warm_air:
        x, y = map(lambda x: sum(x), zip([x, y], dist[kind][1]))
        board[x][y] += 5
        dq = deque([(x, y, 4)])
        visited = set()
        while dq:
            cx, cy, val = dq.popleft()
            if val == 0:
                continue
            for dx, dy, nkind in dist[kind]:
                # 벽으로 막혀있다면
                nx, ny = cx + dx, cy + dy
                if not valid_check(nx, ny):
                    continue
                if (nx, ny, t[kind]) in walls or (cx, cy, nkind) in walls or (nx, ny) in visited:
                    continue

                dq.append((nx, ny, val - 1))
                board[nx][ny] += val
                visited.add((nx, ny))

def mediate_temp(walls) -> None:
    """
    두 칸의 온도의 차이 / 4 (내림) => 그냥 연산하면 된다.
    """
    new_board = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] == 0:
                continue
            # 위
            if 0 <= i-1 < R and (i, j, UP) not in walls:
                val = (board[i][j] - board[i-1][j]) // 4
                if val > 0:
                    new_board[i-1][j] += val
                    new_board[i][j] += -val
            # 아래
            if 0 <= i+1 < R and (i, j, DOWN) not in walls:
                val = (board[i][j] - board[i+1][j]) // 4
                if val > 0:
                    new_board[i+1][j] += val
                    new_board[i][j] += -val
            # 왼
            if 0 <= j-1 < C and (i, j, LEFT) not in walls:
                val = (board[i][j] - board[i][j-1]) // 4
                if val > 0:
                    new_board[i][j-1] += val
                    new_board[i][j] += -val
            # 오른
            if 0 <= j+1 < C and (i, j, RIGHT) not in walls:
                val = (board[i][j] - board[i][j+1]) // 4
                if val > 0:
                    new_board[i][j+1] += val
                    new_board[i][j] += -val
    
    for i in range(R):
        for j in range(C):
            board[i][j] += new_board[i][j]

def down_temp() -> None:
    for i in [0, R-1]:
        for j in range(C):
            if board[i][j] > 0:
                board[i][j] -= 1
    
    for j in [0, C-1]:
        for i in range(1, R-1):
            if board[i][j] > 0:
                board[i][j] -= 1

def check(check_area : List[Tuple[int, int]]) -> bool:
    for x, y in check_area:
        if board[x][y] < K:
            return False
    return True

def solution(warm_air : List[Tuple[int, int, int]], walls : Set[Tuple[int, int, int]], check_area : List[Tuple[int, int]]):
    global board
    board = [[0] * C for _ in range(R)]
    answer = 0
    while True:
        onair(warm_air, walls)
        mediate_temp(walls)
        down_temp()
        # eat
        answer += 1
        if answer > 100:
            return 101
        if check(check_area):
            for i in board:
                print(*i)
            return answer

if __name__ == "__main__":
    R, C, K = map(int, input().split())
    """
    벽 check는 집합으로.
    왼쪽 오른쪽으로 갈때는 1
    위쪽 아래는 0
    """
    warm_air = []
    check_area = []
    for x in range(R):
        for y, val in enumerate(map(int, input().split())):
            if val == 5:
                check_area.append((x, y))
            elif val != 0:
                warm_air.append((x, y, val))

    W = int(input())
    walls = set()
    for _ in range(W):
        x, y, val = map(int, input().split())
        if val == 0:
            walls.add((x-1, y-1, UP))
            walls.add((x-2, y-1, DOWN))
        elif val == 1:
            walls.add((x-1, y-1, RIGHT))
            walls.add((x-1, y, LEFT))

    result = solution(warm_air, walls, check_area)
    print(result)
