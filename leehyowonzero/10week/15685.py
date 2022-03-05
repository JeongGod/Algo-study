from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N = int(input())
arr = [[0 for _ in range(101)] for i in range(101)]
for i in range(N):
    x, y, d, g = map(int, input().split())
    arr[x][y] = 1
    now_dir = [d]
    x += dx[d]
    y += dy[d]
    arr[x][y] = 1
    for _ in range(g):
        for i in range(len(now_dir) - 1, -1, -1):
            x += dx[(now_dir[i] + 1) % 4]
            y += dy[(now_dir[i] + 1) % 4]
            arr[x][y] = 1
            now_dir.append((now_dir[i] + 1) % 4)

result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i][j + 1] and arr[i + 1][j] and arr[i + 1][j + 1]:
            result += 1
print(result)
