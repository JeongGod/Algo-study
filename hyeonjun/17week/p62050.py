from heapq import heappush, heappop

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solution(land, height):
    def divide_map(x, y, target_height):
        land[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and land[nx][ny]:
                if abs(target_height - land[nx][ny]) > height:
                    heappush(
                        queue, (abs(target_height - land[nx][ny]), nx, ny))
                else:
                    heappush(queue, (0, nx, ny))
    N = len(land)
    total_cost = 0
    queue = [(0, 0, 0)]
    while queue:
        cost, x, y = heappop(queue)
        if land[x][y]:
            divide_map(x, y, land[x][y])
            total_cost += cost

    return total_cost
