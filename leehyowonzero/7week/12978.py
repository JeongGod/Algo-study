import heapq

def dijkstra(dist, node):
    heap = []
    heapq.heappush(heap, [0, 1])  # [dist, 노드idx]
    while heap:
        cost, nodeidx = heapq.heappop(heap)
        for to, value in node[nodeidx]:
            if cost + value < dist[to]:
                dist[to] = cost + value
                heapq.heappush(heap, [cost + value, to])
                               
def solution(N, road, K):
    dist = [float('inf') for _ in range(N+1)]
    dist[1] = 0  
    node = [[] for _ in range(N+1)]
    
    for fm, to, value in road:
        node[fm].append([to, value])
        node[to].append([fm, value])
        
    dijkstra(dist,node)
    
    return len([i for i in dist if i <=K])