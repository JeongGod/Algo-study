import sys
from collections import deque

input = sys.stdin.readline

cnt = 0
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
EAST, SOUTH,  WEST, NORTH = 0, 1, 2, 3
"""
1 : 0 <=> 2
2 : 1 <=> 3
3 : 0 <=> 3, 2 <=> 1
4 : 0 <=> 1, 2 <=> 3
"""
def check(x, y):
    return 0 <= x < N and 0 <= y < M

def search(board, air):
    # (왼쪽 오른쪽), (위 아래)
    visited = [[[False, False, False, False] for _ in range(M)] for _ in range(N)]

    for x, y in air:
        for i in range(4):
            visited[x][y][i] = True
        for go, (gx, gy) in enumerate(zip(dx, dy)):
            nx, ny = x + gx, y + gy
            while check(nx, ny) and not visited[nx][ny][go]:
                visited[nx][ny][go] = True
                if board[nx][ny] == 1:
                    if go%2 == 0:
                        continue
                elif board[nx][ny] == 2:
                    if go%2 == 1:
                        continue
                elif board[nx][ny] == 3:
                    if go%2 == 0:
                        go = (go-1)%4
                    else:
                        go = (go+1)%4
                elif board[nx][ny] == 4:
                    if go%2 == 0:
                        go += 1
                    else:
                        go -= 1
                nx, ny = nx + dx[go], ny + dy[go]
                
    cnt = 0
    for i in visited:
        for a in i:
            if any(a):
                cnt += 1
        
    return cnt

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = []
    air = []
    for x in range(N):
        tmp = list(map(int, input().split()))
        for y in range(M):
            if tmp[y] == 9:
                air.append((x, y))
        board.append(tmp)

    print(search(board, air))
