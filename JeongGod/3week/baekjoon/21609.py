from re import L
import sys
from typing import List, Set, Tuple
from collections import deque
input = sys.stdin.readline


"""
black은 변하지 중력의 영향을 받지 않는다. 90도로 변환하면서 진행하자.

기준 블록 = 행의 번호가 가장 작은 블록, 열의 번호가 가장 작은 블록
"""

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def gravity() -> None:
    st = []
    for y in range(N):
        for x in range(N):
            if board[x][y] == " ":
                continue
            st.append((board[x][y], x))
            board[x][y] = " "
        # 보드에 넣자.
        x = N-1
        while st:
            val, idx = st.pop()
            # 만일 black 블록이면 행의 위치를 해당 부터 채워넣는걸로 변경한다.
            if val == -1:
                x = idx
            board[x][y] = val
            x -= 1


def rotate() -> List:
    new_board = [[0] * N for _ in range(N)]
    # 보드 회전
    # (x, y) -> (N-1-y, x)
    for x in range(N):
        for y in range(N):
            new_board[N-1-y][x] = board[x][y]
    
    return new_board

def bfs(x : int, y : int) -> int:
    val = board[x][y]
    dq = deque([(x, y)])
    visited = {(x, y)}

    rainbow = 0

    while dq:
        cx, cy = dq.popleft()
        for idx in range(4):
            nx, ny = cx + dx[idx], cy + dy[idx]
            # 벗어났다면
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            # (무지개 블록이거나 같은 색 블록이 아님) or (검은색 블록임) or (방문한 적이 있다면)
            if not (board[nx][ny] == 0 or board[nx][ny] == val) or board[nx][ny] == -1 or (nx, ny) in visited:
                continue
            # 무지개 블록의 개수를 세준다.
            if board[nx][ny] == 0:
                rainbow += 1
            visited.add((nx, ny))
            dq.append((nx, ny))
    return visited, rainbow

def check(visited : Set, rainbow_cnt : int, max_block_group : Set) -> bool:
    if len(visited) < len(max_block_group[0]):
        return False
    elif len(visited) > len(max_block_group[0]):
        return True
    else:
        if rainbow_cnt >= max_block_group[1]:
            return True
        else:
            return False
    

def main() -> int:    
    global N, board, black_pos
    score = 0
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    while True:
        visited_block = set()
        max_block_group = [set(), 0]
        # 블록 탐색
        for x in range(N):
            for y in range(N):
                if board[x][y] == -1 or board[x][y] == 0 or board[x][y] == " ":
                    continue
                if (x, y) in visited_block:
                    continue
                visited, rainbow_cnt = bfs(x, y)
                visited_block |= visited
                if check(visited, rainbow_cnt, max_block_group):
                    max_block_group[0] = visited
                    max_block_group[1] = rainbow_cnt
        # 종료 조건
        if len(max_block_group[0]) < 2:
            break

        # 블록 부수기
        for x, y in max_block_group[0]:
            board[x][y] = " "
        # 중력
        gravity()
        # 회전
        board = rotate()
        # 중력
        gravity()
        # 점수 계산
        score += len(max_block_group[0]) ** 2
        
    return score

if __name__ == "__main__":
    print(main())
