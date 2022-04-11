import heapq
import sys

input = sys.stdin.readline


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check(x : int, y : int) -> bool :
    return 0 <= x < N and 0 <= y < M

def trash_check(x : int, y : int) -> bool:
    for gx, gy in zip(dx, dy):
        nx, ny = x + gx, y + gy
        if not check(nx, ny):
            continue
        if board[nx][ny] == "g":
            return True
    return False

def solution(board : list[list[str]], start : list[int, int], end : list[int, int]) -> tuple[int, int]:
    visited = [[[False, sys.maxsize, sys.maxsize] for _ in range(M)] for _ in range(N)]
    hq = [(0, 0, *start)]
    
    cnt = 0
    while hq:
        cnt += 1
        trash, side, cx, cy = heapq.heappop(hq)

        # 도착
        if cx == end[0] and cy == end[1]:
            side -= trash_check(cx, cy)
            return trash, side
        # 이미 방문했던 곳이라면 패스
        if visited[cx][cy][0] and visited[cx][cy][1] < trash and visited[cx][cy][2] < side:
            continue
        # 방문을 해보자.
        for gx, gy in zip(dx, dy):
            nx, ny = cx + gx, cy + gy
            n_trash = trash
            n_side = side
            if not check(nx, ny):
                continue
            if board[nx][ny] == "g":
                n_trash += 1
            else:
                n_side += 1 if trash_check(nx, ny) else 0
            
            if visited[nx][ny][0] and visited[nx][ny][1] <= n_trash and visited[nx][ny][2] <= n_side:
                continue
            visited[nx][ny][0] = True
            visited[nx][ny][1] = n_trash
            visited[nx][ny][2] = n_side
            heapq.heappush(hq, (n_trash, n_side, nx, ny))


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    start = [0, 0]
    end = [0, 0]
    for x in range(N):
        for y in range(M):
            if board[x][y] == "S":
                start = [x, y]
            elif board[x][y] == "F":
                end = [x, y]
    print(*solution(board, start, end))
