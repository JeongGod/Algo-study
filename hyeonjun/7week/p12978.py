from heapq import heappush, heappop


def dijkstra(start, N, bridge):
    distances = {i: float('inf') for i in range(1, N+1)}
    distances[start] = 0
    queue = []
    heappush(queue, (distances[start], start))
    while queue:
        current_dist, node = heappop(queue)
        if distances[node] < current_dist:
            continue
        for adj_node, dist in bridge[node].items():
            weighted_dist = current_dist + dist
            if weighted_dist < distances[adj_node]:
                distances[adj_node] = weighted_dist
                heappush(queue, (weighted_dist, adj_node))
    return distances


def solution(N, road, K):
    answer = 0
    road.sort(key=lambda x: -x[2])
    bridge = {i: {} for i in range(1, N+1)}
    for s, e, dist in road:
        bridge[s][e] = dist
        bridge[e][s] = dist
    distances = dijkstra(1, N, bridge)
    for key, value in distances.items():
        if value <= K:
            answer += 1

    return answer
