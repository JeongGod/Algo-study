import sys
from collections import deque
from itertools import islice

input = sys.stdin.readline
"""
1. N은 항상 홀수
2. 마법사 상어는 (N+1)/2, (N+1)/2에 존재
3. 벽 존재

1. 상어가 있는 칸 제외 구슬이 들어간다.
2. 같은 번호가 들어간 구슬은 연속하는 구슬이라고 한다.
3. 블리자드 마법은 방향과 거리가 존재한다. 벽은 파괴되지 않는다.
4. 구슬은 이동한다. A의 번호보다 번호가 하나 작은 칸이 빈칸이라면.
"""

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def blizard_skill(shark : tuple[int, int], d : int, s : int) -> None:
    cx, cy = shark
    for i in range(1, s+1):
        board[cx + dx[d] * i][cy + dy[d] * i] = 0

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
PUT, OUT = 0, 1
def search_board(shark : tuple[int, int], mode : int, dq : deque[int] = None):
    """
    (0, 0)부터 shark자리가 있는데까지 돌면서 모든 구슬을 흝어본다.
    """
    visited = [[False] * N for _ in range(N)]
    go_list = [RIGHT, DOWN, LEFT, UP]
    cx, cy = 0, 0
    go = 0
        
    # 방문했는지, 보드안에 있는지 체크
    def check(x, y):
        return 0 <= x < N and 0 <= y < N and not visited[x][y]
    # shark자리가 있는데 까지 모든 구슬을 흝는다.
    while cx != shark[0] or cy != shark[1]:
        
        # 모드 확인
        # 담는 모드이면 담는다.
        if mode == PUT:
            if board[cx][cy] != 0:
                dq.append(board[cx][cy])

        # 내보내는거면 내보낸다.
        elif mode == OUT:
            if not dq:
                break
            board[cx][cy] = dq.popleft()

        visited[cx][cy] = True
        nx, ny = cx + dx[go_list[go]], cy + dy[go_list[go]]
        if not check(nx, ny):
            go = (go + 1) % 4
            nx, ny = cx + dx[go_list[go]], cy + dy[go_list[go]]
        cx, cy = nx, ny
    if mode == PUT:
        return dq
    elif mode == OUT:
        return None

def bring_marbles(shark : tuple[int, int]) -> None:
    """
    stack 으로 담아서 내리는 형식으로 생각하자.
    """
    return search_board(shark, PUT, deque([]))


def delete_marbles(marbles : deque[int]) -> deque[int]:
    # 폭탄 체크한다.
    global answer
    marbles.append(0)
    new_dq = []
    cnt = 0
    a = 0
    before = marbles[0]
    while True:
        flag = False
        new_dq = []
        for val in marbles:
            if val == before:
                cnt += 1
            else:
                if cnt >= 4:
                    flag = True
                    answer += new_dq[-1] * cnt
                    for _ in range(cnt):
                        new_dq.pop()
                cnt = 1
            before = val
            new_dq.append(val)
        marbles = new_dq[:]
        if not flag:
            break
    return deque(marbles)

def change_marbles(marbles : deque[int]) -> deque[int]:
    marbles.append(0)
    # 폭탄을 다 제거했다면 변경한다.
    new_dq = deque([])
    cnt = 0
    before = marbles[0]
    for val in marbles:
        if val == before:
            cnt += 1
        else:
            new_dq.append(before)
            new_dq.append(cnt)
            cnt = 1
        before = val
    return new_dq

def insert_marbles(shark : tuple[int, int], marbles : deque[int]) -> None:
    # 남는 자리는 0으로 추가한다.
    for _ in range((N*N) - 1 - len(marbles)):
        marbles.appendleft(0)
    # 커지면 그외 나머지는 자른다.
    if len(marbles) > N*N - 1:
        marbles = deque(islice(marbles, len(marbles) - N*N + 1, len(marbles)+1))
    search_board(shark, OUT, marbles)
    
def solution(skills : list[tuple[int, int]]) -> int:
    global answer
    answer = 0
    shark = (N//2, N//2)
    for d, s in skills:
        blizard_skill(shark, d, s)
        marbles = bring_marbles(shark)
        marbles = delete_marbles(marbles=marbles)
        marbles = change_marbles(marbles=marbles)
        insert_marbles(shark=shark, marbles=marbles)
    
    return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    def change_to_dist(x):
        return int(x)
    board = [list(map(int, input().split())) for _ in range(N)]
    skills = []
    for _ in range(M):
        d, s = map(int, input().split())
        skills.append((d-1, s))
    print(solution(skills))
