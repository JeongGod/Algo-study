from collections import defaultdict


def solution(n, s, a, b, fares):
    def floyd_warshall():
        dist = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] or i == j:
                    dist[i][j] = graph[i][j]
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist

    graph = {i: defaultdict(int) for i in range(1, n+1)}
    for node1, node2, fee in fares:
        graph[node1][node2] = fee
        graph[node2][node1] = fee
    dist = floyd_warshall()

    answer = dist[s][a] + dist[s][b]
    for node in range(1, n+1):
        answer = min(answer, dist[s][node] + dist[node][a] + dist[node][b])

    return answer
