def solution(n):
    answer = []
    dir = [(1, 0), (0, 1), (-1, -1)]
    board = [[0] * n for _ in range(n)]
    target = 0
    for i in range(1, n+1):
        target += i
    x, y = 0, 0
    cnt = 1
    board[x][y] = cnt
    d = 0
    while True:
        nx, ny = x + dir[d][0], y + dir[d][1]
        if (0 <= nx < n and 0 <= ny < n) and board[nx][ny] == 0:
            cnt += 1
            board[nx][ny] = cnt
            x, y = nx, ny
        else:
            d += 1
            d %= 3
        if cnt == target:
            break
    board[x][y] = cnt
    for b in board:
        for el in b:
            if el != 0:
                answer.append(el)
    return answer