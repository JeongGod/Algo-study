from collections import deque
import sys

def solution(N, road, K):
  nodes = {}
  dist = {i:sys.maxsize for i in range(1, N+1)}
  dist[1] = 0

  for v1, v2, d in road:
    nodes[v1] = nodes.get(v1, []) + [(v2, d)]
    nodes[v2] = nodes.get(v2, []) + [(v1, d)]
    
  dq = deque([1])
  while dq:
    curr_node = dq.popleft()
    for next_node, d in nodes[curr_node]:
      if dist[next_node] > dist[curr_node] + d:
        dist[next_node] = dist[curr_node] + d
        dq.append(next_node)

  return len([v for v in dist.values() if v <= K])