import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

min_heap = []
max_heap = []
is_solved = defaultdict(bool)
n = int(input())
for _ in range(n):
  p, l = map(int, input().split(' '))
  heapq.heappush(min_heap, (l, p))
  heapq.heappush(max_heap, (-l, -p))
  is_solved[p] = True

m = int(input())
for _ in range(m):
  cmd = input().split()
  if cmd[0] == 'add':
    while not is_solved[-max_heap[0][1]]:
      heapq.heappop(max_heap)
    while not is_solved[min_heap[0][1]]:
      heapq.heappop(min_heap)
    is_solved[int(cmd[1])] = True
    heapq.heappush(max_heap,(-int(cmd[2]), -int(cmd[1])))
    heapq.heappush(min_heap,(int(cmd[2]), int(cmd[1])))
  elif cmd[0] == 'recommend':
    if cmd[1] == '1':
      while not is_solved[-max_heap[0][1]]:
        heapq.heappop(max_heap)
      print(-max_heap[0][1])
    else:
      while not is_solved[min_heap[0][1]]:
        heapq.heappop(min_heap)
      print(min_heap[0][1])
  elif cmd[0] == 'solved':
    is_solved[int(cmd[1])] = False