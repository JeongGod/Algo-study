"""
1. 2^n, 2^n 회전
2. 얼음이 녹는다.
    => board[x][y]의 상하좌우를 살핀다 => 얼음이 있는 칸이 >= 3 이 아니라면 board[x][y] - 1

==> 결과
    1. 총 얼음의 합
    2. 얼음이 연결되어있는 칸의 개수(가장 큰 것)
"""
import sys
from collections import deque
from typing import List

input = sys.stdin.readline

def rotate(x : int, y : int, l : int, cnt : int) -> None:
    new_board = []
    
    for j in range(y, y+2**l):
        tmp = [board[i][j] for i in range(x+2**l - 1, x-1, -1)]
        new_board.append(tmp)
    
    for i in range(2**l):
        for j in range(2**l):
            board[x+i][y+j] = new_board[i][j]

def is_ice(x : int, y : int) -> int:
    if not (0 <= x < 2**N and 0 <= y < 2**N):
        return 0
    if board[x][y] == 0:
        return 0
    return 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def melt_ice() -> None:
    tmp = []
    for i in range(2**N):
        for j in range(2**N):
            cnt = 0
            for gx, gy in zip(dx, dy):
                cnt += is_ice(i+gx, j+gy)
            if cnt >= 3:
                continue
            tmp.append((i, j))
    for i, j in tmp:
        if board[i][j] == 0:
            continue
        board[i][j] -= 1

def count_iceblock(x : int, y : int, visited : List[List[int]]) -> int:
    dq = deque([(x, y)])
    cnt = 0
    while dq:
        cx, cy = dq.popleft()
        cnt += 1
        for gx, gy in zip(dx, dy):
            nx, ny = cx + gx, cy + gy
            if not is_ice(nx, ny) or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            dq.append((nx, ny))
    return cnt

def solution(cnt : int) -> List[int]:
    levels = list(map(int, input().split()))
    for idx in range(cnt):
        l = levels[idx]
        # 회전의 시작점을 잡아준다.
        for i in range(0, 2**N, 2**l):
            for j in range(0, 2**N, 2**l):
                rotate(i, j, l, 0)
        melt_ice()

    visited = [[False] * len(board) for _ in range(len(board))]
    answer = [0, 0]

    for i in range(2**N):
        for j in range(2**N):
            answer[0] += board[i][j]
            if not is_ice(i, j) or visited[i][j]:
                continue
            visited[i][j] = True
            answer[1] = max(answer[1], count_iceblock(i, j, visited))
    
    return answer


if __name__ == "__main__":
    N, Q = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(2**N)]
    
    print("\n".join(map(str, solution(Q))))
