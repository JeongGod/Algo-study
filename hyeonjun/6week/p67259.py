from collections import deque


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def bfs(board):
    length = len(board)
    queue = deque()
    queue.append((0, 0, 0, -1))
    visited = [[[float('inf') for _ in range(4)]
                for _ in range(length)] for _ in range(length)]
    visited[0][0] = [0, 0, 0, 0]

    while queue:
        x, y, cost, direction = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < length and 0 <= ny < length and board[nx][ny] != 1:
                if i == direction or direction == -1:
                    tmp_cost = cost + 100
                else:
                    tmp_cost = cost + 600
                if visited[nx][ny][i] <= tmp_cost:
                    continue

                visited[nx][ny][i] = tmp_cost
                queue.append((nx, ny, tmp_cost, i))

    return min(visited[length-1][length-1])


def solution(board):
    return bfs(board)
