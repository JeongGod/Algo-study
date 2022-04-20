import copy
import sys

input = sys.stdin.readline

def rotate(board : list[list[int]]) -> list[list[int]]:
    cboard = []
    height, row = len(board), len(board[0])
    for y in range(row):
        cboard.append([board[x][y] for x in range(height-1, -1, -1)])
    return cboard

def insert_check(x : int, y : int, tboard : list[list[int]], board : list[list[int]]) -> int:
    # board에 tboard를 넣는다.
    theight, trow = len(tboard), len(tboard[0])
    iheight, irow = len(board), len(board[0])
    for i in range(theight):
        for j in range(trow):
            # 범위를 벗어나는 경우 가능하다고 판단 -> 현재 row, height값을 하나 증가시킨다.
            if not(0 <= x+i < iheight):
                iheight += 1
            if not(0 <= y+j < irow):
                irow += 1
            if not(0 <= x+i < len(board) and 0 <= y+j < len(board[0])):
                continue
            # 안되는 경우
            if board[x+i][y+j] + tboard[i][j] == 2:
                return sys.maxsize
    return iheight * irow

def solution(b1 : list[list[int]], b2 : list[list[int]]) -> int:
    """
    1. 큰 보드를 기준으로 놓고 작은 보드를 끼워넣는 식
    2. 50*50 0인곳에 꽃아본다. = 2500 * 2500 = 6250000
    3. 4군데를 돌려보면서 꽃아본다. = 6250000*4
    """
    rotate_b1 = [copy.deepcopy(b1)]
    for i in range(3):
        rotate_b1.append(rotate(rotate_b1[i]))
    # b2를 돌려놓는다.
    rotate_b2 = [copy.deepcopy(b2)]
    for i in range(3):
        rotate_b2.append(rotate(rotate_b2[i]))
    
    # b1을 기준
    answer = sys.maxsize
    for board in rotate_b1:
        for tboard in rotate_b2:
            for x in range(len(board)+1):
                for y in range(len(board[0])+1):
                    # 끼워넣어본다.
                    answer = min(answer, insert_check(x, y, tboard, board))

    return answer

if __name__ == "__main__":
    N1, M1 = map(int, input().split())
    puzzle1 = [list(map(int, input().rstrip())) for _ in range(N1)]
    N2, M2 = map(int, input().split())
    puzzle2 = [list(map(int, input().rstrip())) for _ in range(N2)]
    print(min(solution(puzzle1, puzzle2), solution(puzzle2, puzzle1)))
