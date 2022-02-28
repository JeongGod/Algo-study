import sys

input = sys.stdin.readline

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
CLEAN = 2
def check(x : int, y : int) -> bool:
    return 0 <= x <= N and 0 <= y <= M and board[x][y] == 0
    

def solution(x : int, y : int, go : int, board : list[list[int]]) -> int:
    """
    1. 현재 위치를 청소한다.
    왼쪽이 비었다면 전진
    왼쪽 아래 오른쪽 위순으로 확인

    모두 청소가 되어있다면 한 칸 후진
    뒤쪽 방향도 못간다면 작동을 멈춘다.
    """
    board[x][y] = CLEAN
    answer = 1
    while True:
        # 체크했을 때 청소가 가능하다면
        for _ in range(4):
            go = (go+3) % 4
            nx, ny = x + dx[go], y + dy[go]
            
            # 청소가 된다면
            if check(nx, ny):
                x, y = nx, ny
                board[x][y] = CLEAN
                answer += 1
                break
        else:
            # 청소가 되지 않았다면 후진을 해본다.
            x, y = x + dx[(go+2)%4], y + dy[(go+2)%4]
            if board[x][y] == 1:
                return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    x, y, go = map(int, input().split())

    board = list(list(map(int, input().split())) for _ in range(N))
    print(solution(x, y, go, board))

