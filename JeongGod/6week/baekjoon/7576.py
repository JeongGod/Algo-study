import sys
from collections import deque
from typing import List, Tuple

input = sys.stdin.readline

def check(x : int, y : int) -> bool:
    if not(0 <= x < M and 0 <= y < N):
        return False
    return True

def solution(dq : List[Tuple[int, int]], board : List[List[int]]) -> int:
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    while dq:
        cx, cy, days = dq.popleft()
        for gx, gy in zip(dx, dy):
            nx, ny = cx + gx, cy + gy
            if not check(nx, ny):
                continue
            if board[nx][ny] == -1 or board[nx][ny] == 1:
                continue
            board[nx][ny] = 1
            dq.append((nx, ny, days+1))

    for i in range(M):
        for j in range(N):
            if board[i][j] == 0:
                return -1
    return days

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = []
    dq = deque([])
    for i in range(M):
        tmp = list(map(int, input().split()))
        board.append(tmp)
        for j in range(len(tmp)):
            # 토마토가 있는 것을 저장한다.
            if tmp[j] == 1:
                dq.append((i, j, 0))
    print(solution(dq, board))
