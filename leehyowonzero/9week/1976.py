from collections import deque

N = int(input())
M = int(input())
edge = []
for _ in range(N):
    edge.append(list(map(int, input().split())))
plan = list(map(int, input().split()))

visited = [False for _ in range(N)]
q = deque()
q.append(plan[0]-1)
visited[plan[0]-1] = True
while q :
    now = q.popleft()
    for i in range(N):
        if(edge[now][i] == 1 and visited[i] == False):
            q.append(i)
            visited[i] = True

for el in plan:
    if(visited[el-1] == False):
        print("NO")
        exit(0)
print("YES")