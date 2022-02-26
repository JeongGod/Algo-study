# from collections import deque

# n = int(input())
# m = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
# plan = list(map(int, input().split()))

# visited = [False * n for _ in range(n)]
# dq = deque()
# dq.append(plan[0]-1)
# visited[plan[0]-1] = True
# while dq:
#   curr = dq.popleft()
#   for i in range(n):
#     if board[curr][i] == 1 and not visited[i]:
#       visited[i] = True
#       dq.append(i)

# for p in plan:
#   if not visited[p-1]:
#     print('NO')
#     exit(0)
# print('YES')

n = int(input())
m = int(input())
parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i

def find(a):
  if a == parent[a]:
    return a
  p = find(parent[a])
  parent[a] = p
  return parent[a]

def union(a, b):
  a = find(a) 
  b = find(b) 

  if a == b:
    return
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
print(parent)
for i in range(1, n+1):
  board = list(map(int, input().split()))
  for j in range(1, len(board) + 1):
    if board[j-1] == 1:
      union(i,j)
      print(parent)
plan = list(map(int, input().split()))
res = set([find(i) for i in plan])
if len(res) != 1:
  print('NO')
else:
  print('YES')