from collections import deque

SQUARE = [(0, 1), (1, 0), (1, 1)]


def solution(m, n, board):
    answer = 0
    for idx in range(len(board)):
        board[idx] = list(board[idx])

    def gravity():
        for i in range(n):
            cand = deque()
            for j in range(m-1, -1, -1):
                if not board[j][i]:
                    cand.append((j, i))
                elif cand:
                    x, y = cand.popleft()
                    board[x][y] = board[j][i]
                    board[j][i] = 0
                    cand.append((j, i))

    def delete_block(target_arr):
        for x, y in target_arr:
            board[x][y] = 0

    def dfs():
        delete_list = set()
        for x in range(m):
            for y in range(n):
                target = board[x][y]
                if target and target >= 'A' and target <= 'Z':
                    flag = True
                    for i in SQUARE:
                        nx = x + i[0]
                        ny = y + i[1]
                        if nx >= m or ny >= n or board[nx][ny] != target:
                            flag = False
                            break
                    if flag:
                        delete_list.update(
                            [(x, y), (x, y+1), (x+1, y), (x+1, y+1)])
        return delete_list

    while True:
        delete_list = dfs()
        if not delete_list:
            break
        answer += len(delete_list)
        delete_block(delete_list)
        gravity()

    return answer
