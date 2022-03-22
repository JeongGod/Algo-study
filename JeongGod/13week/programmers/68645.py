dx = [1, 0, -1]
dy = [0, 1, -1]

def solution(n):
    def check(x, y):
        return 0 <= x < n and 0 <= y < n
    
    answer = []
    board = [[0]*n for _ in range(n)]
    
    if n == 1:
        return [1]
    
    x, y = 0, 0
    go = 0
    val = 1
    while True:
        board[x][y] = val
        nx, ny = x + dx[go], y + dy[go]
        # 보드밖이거나 방문했을 경우
        if not check(nx, ny) or board[nx][ny]:
            # 방향을 바꿔서 간다.
            go = (go+1) % 3
            nx, ny = x + dx[go], y + dy[go]
        # 방향을 바꿨는데도 방문한 곳이라면
        if board[nx][ny]:
            break
        val += 1
        x, y = nx, ny
    
    for i in range(1, n+1):
        answer += board[i-1][:i]
    return answer
