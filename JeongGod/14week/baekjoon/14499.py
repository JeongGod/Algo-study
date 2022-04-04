"""
1. 바닥면이 0 인경우
    => 주사위의 바닥 면의 수가 복사된다.
2. 바닥면이 0이 아닌 경우
    => 주사위의 바닥 면으로 숫자가 옮겨간다.
    바닥면은 0이 된다.

"""
import sys
from collections import deque

input = sys.stdin.readline

dist = {
    1 : (0, 1),
    2 : (0, -1),
    3 : (-1, 0),
    4 : (1, 0)
}
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

class Dice:
    def __init__(self):
        self.side = deque([0, 0, 0, 0])
        self.upside = deque([0, 0, 0, 0])

    def __side_sync(self):
        self.upside[0] = self.side[0]
        self.upside[2] = self.side[2]

    def __upside_sync(self):
        self.side[0] = self.upside[0]
        self.side[2] = self.upside[2]
    # 오른쪽으로 굴린다.
    def right(self):
        self.side.appendleft(self.side.pop())
        self.__side_sync()
    
    def left(self):
        self.side.append(self.side.popleft())
        self.__side_sync()
        
    
    def up(self):
        self.upside.append(self.upside.popleft())
        self.__upside_sync()
    
    def down(self):
        self.upside.appendleft(self.upside.pop())
        self.__upside_sync()

def check(x : int, y : int) -> bool:
    return 0 <= x < N and 0 <= y < M

def solution(n : int, m : int, x : int, y : int, board : list[list[int]], commands : list[int]):
    dice = Dice()
    cx, cy = x, y
    for com in commands:
        
        nx, ny = cx + dx[com-1], cy + dy[com-1]
        if not check(nx, ny):
            continue
        # 현재 바닥면 처리
        if board[cx][cy] == 0:
            board[cx][cy] = dice.upside[0]
        else:
            dice.upside[0] = board[cx][cy] 
            dice.side[0] = board[cx][cy]
            board[cx][cy] = 0
        
        if com == 1:
            dice.right()
        elif com == 2:
            dice.left()
        elif com == 3:
            dice.up()
        elif com == 4:
            dice.down()
        cx, cy = nx, ny
        print(dice.side[2])
        

if __name__ == "__main__":
    N, M, x, y, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    commands = list(map(int, input().split()))
    solution(N, M, x, y, board, commands)
