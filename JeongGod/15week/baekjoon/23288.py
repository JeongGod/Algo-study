import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(x : int, y : int) -> bool:
    return 0 <= x < N and 0 <= y < M

def bfs(board : list[list[int]], x : int, y : int):
    global visited
    val = board[x][y]
    dq = deque([(x, y)])
    search = [(x, y)]
    while dq:
        cx, cy = dq.popleft()
        for gx, gy in zip(dx, dy):
            nx, ny = cx + gx, cy + gy
            if not check(nx, ny) or visited[nx][ny]:
                continue
            if board[nx][ny] != val:
                continue
            visited[nx][ny] = True
            search.append((nx, ny))
            dq.append((nx, ny))
    # 값을 board에 추가한다.
    for a, b in search:
        board[a][b] = [val, len(search)]
    return board

def find_possible_move(board : list[list[int]]) -> list[list[list[int, int]]]:
    global visited
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if visited[x][y]:
                continue
            visited[x][y] = True
            bfs(board, x, y)
    return board

class Dice:
    def __init__(self):
        self.side = deque([6,4,1,3])
        self.up = deque([6,5,1,2])
    
    def rotate(self, case : int):
        # 북
        if case == 0:
            self.up.appendleft(self.up.pop())
            self.side[0], self.side[2] = self.up[0], self.up[2]
        # 동
        elif case == 1:
            self.side.appendleft(self.side.pop())
            self.up[0], self.up[2] = self.side[0], self.side[2]
        # 남
        elif case == 2:
            self.up.append(self.up.popleft())
            self.side[0], self.side[2] = self.up[0], self.up[2]
        # 서
        elif case == 3:
            self.side.append(self.side.popleft())
            self.up[0], self.up[2] = self.side[0], self.side[2]
def solution(board : list[list[int]], move : int) -> int:
    """
    1. BFS를 통해 각 보드에서 이동할 수 있는 칸의 수 C를 구한다.
    2. 주사위를 굴리면서 구현한다.
    """
    # 움직일 수 있는 보드를 새로 만들어놓는다.
    new_board = find_possible_move(board)
    # 주사위를 굴린다.
    dice = Dice()
    go = 1
    cx, cy = 0, 0
    score = 0
    for _ in range(move):
        nx, ny = cx + dx[go], cy + dy[go]
        # 만약 칸이 없다면 반대 방향으로 이동한다.
        if not check(nx, ny):
            go = (go + 2) % 4
            nx, ny = cx + dx[go], cy + dy[go]
        # 주사위를 굴린다.
        dice.rotate(go)
        # 점수를 획득한다.
        board_val, board_cnt = new_board[nx][ny][0], new_board[nx][ny][1]
        score += board_val * board_cnt
        # 이동 방향을 결정한다.
        bottom = dice.side[0]
        if bottom > board_val:
            go = (go + 1) % 4
        elif bottom < board_val:
            go = (go - 1) % 4
        cx, cy = nx, ny
    return score

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    print(solution(board, K))
