import heapq
import sys


def solution(N, road, K):
    graph = [[] for _ in range(N)]
    for x, y, cost in road:
        graph[x-1].append((y-1, cost))
        graph[y-1].append((x-1, cost))
    
    visited = [sys.maxsize] * N
    hq = [(0, 0)]
    while hq:
        c_cost, cur = heapq.heappop(hq)
        if c_cost >= visited[cur]:
            continue
        visited[cur] = c_cost
        for n_dest, n_cost in graph[cur]:
            cost = c_cost + n_cost
            if visited[n_dest] <= cost:
                continue
            heapq.heappush(hq, (cost, n_dest))

    return len(list(filter(lambda x: x<=K, visited)))
