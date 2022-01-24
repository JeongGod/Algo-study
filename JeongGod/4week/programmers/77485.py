from collections import deque


def check(a : int, b : int) -> bool:
    if a < b:
        return True
    return False

def save(x : int, y : int, tx : int, ty : int) -> int:
    result = 10000
    tmp = board[x-1][y-1]
    # 아래 => 위
    for i in range(x-1, tx-1):
        board[i][y-1] = board[i+1][y-1]
        if check(board[i+1][y-1], result):
            result = board[i+1][y-1]
    # 오른 => 왼
    for i in range(y-1, ty-1):
        board[tx-1][i] = board[tx-1][i+1]
        if check(board[tx-1][i+1], result):
            result = board[tx-1][i]
    # 위 => 아래
    for i in range(tx - 1, x-1, -1):
        board[i][ty-1] = board[i-1][ty-1]
        if check(board[i-1][ty-1], result):
            result = board[i-1][ty-1]
    # 왼 => 오
    for i in range(ty - 1, y, -1):
        board[x-1][i] = board[x-1][i-1]
        if check(board[x-1][i-1], result):
            result = board[x-1][i-1]
    board[x-1][y] = tmp
    result = min(tmp, result)
    return result

def solution(rows, columns, queries):
    global board
    """
    1. 시계방향 회전
    2. 테두리의 영역만 회전
    
    1. (x, y), (tx, ty) => 테두리에 있는 값들을 저장해온다.
    2. deque에 저장하고 popleft, append한다.
    3. 다시 값에 넣는다.
    """
    board = [[(j+1) + (i * columns) for j in range(columns)] for i in range(rows)]
    answer = []
    for x, y, tx, ty in queries:
        answer.append(save(x, y, tx, ty))

    return answer
