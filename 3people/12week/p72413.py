import sys
import heapq

def dijkstra(s, e):
  global board, length
  visited = [sys.maxsize] * (length + 1)
  visited[s] = 0
  pq = [(0, s)]
  heapq.heapify(pq)
  
  while pq:
    cost, node = heapq.heappop(pq)
    
    if cost > visited[node]:
      continue

    for n in board[node]:
      next_node, next_cost = n[0], n[1]
      next_cost += cost
      
      if next_cost < visited[next_node]:
        visited[next_node] = next_cost
        heapq.heappush(pq, (next_cost, next_node))
  return visited[e]

def solution(n, s, a, b, fares):
  global board, length
  answer = sys.maxsize
  board = [[] for _ in range(n + 1)]
  length = n
  
  for i, j, cost in fares:
    board[i].append((j, cost))
    board[j].append((i, cost))

  for i in range(1, n + 1):
    answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

  return answer