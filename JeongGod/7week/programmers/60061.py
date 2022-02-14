from typing import List

PILLAR = 0 # 기둥
PAPER  = 1 # 보
LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3

def check_pillar(x : int, y : int, n : int) -> bool:
    # 바닥이거나 보이거나 밑이 기둥이면 세우기 가능하다
    return x == n or PAPER in board[x][y] or PILLAR == board[x][y][DOWN]

def check_paper(x : int, y : int, n : int) -> bool:
    # 양쪽 끝 둘 중에 기둥이 있거나 양쪽 끝 둘 다 보가 존재한다면 가능하다.
    return (PILLAR == board[x][y][DOWN] or PILLAR == board[x][y+1][DOWN]) or\
            (PAPER == board[x][y][LEFT] and PAPER == board[x][y+1][RIGHT])

def check_possible(n : int) -> bool:
    for i in range(n):
        for j in range(n):
            # 기둥인 경우 가능한 지 체크
            if board[i][j][UP] == PILLAR:
                if not check_pillar(i, j, n):
                    return False
            # 보인경우 가능한 지 체크
            if board[i][j][RIGHT] == PAPER:
                if not check_paper(i, j, n):
                    return False
    return True

def command(x : int, y : int, a : int, b : int ,n : int):
    x, y = n-y, x
        
    if a == PILLAR:
        if b == 0:
            board[x][y][UP] = -1
            board[x-1][y][DOWN] = -1
        elif b == 1:
            board[x][y][UP] = PILLAR
            board[x-1][y][DOWN] = PILLAR
    elif a == PAPER:
        if b == 0:
            board[x][y][RIGHT] = -1
            board[x][y+1][LEFT] = -1
        elif b == 1:
            board[x][y][RIGHT] = PAPER
            board[x][y+1][LEFT] = PAPER

        
def solution(n : int, build_frame : List[List[int]]):
    global board
    board = [[[-1, -1, -1, -1] for _ in range(n+1)] for _ in range(n+1)]
    """
    1. 기둥은 바닥 위 or 보의 한쪽 끝 부분 위 or 다른 기둥 위
    2. 보는 한쪽 끝 부분이 기둥 위 or 양쪽 끝 부분이 다른 보와 연결
    """
    for x, y, a, b in build_frame:
        command(x, y, a, b, n)
        # 보드에 넣은 값이 되는지 안 되는지 체크
        if not check_possible(n):
            # 불가능하다면 rollback
            command(x, y, a, abs(b-1), n)
    
    result = []
    for i in range(n+1):
        for j in range(n+1):
            if PILLAR == board[i][j][UP]:
                result.append([j, n-i, PILLAR])
            if PAPER == board[i][j][RIGHT]:
                result.append([j, n-i, PAPER])
    
    return sorted(result)
