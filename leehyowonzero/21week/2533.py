import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def checkdp(idx):
    visited[idx] = True
    for el in edge[idx]:
        if not visited[el]:
            checkdp(el)
            dp[idx][0] += min(dp[el][0], dp[el][1])
            dp[idx][1] += dp[el][0]
    
n = int(input())
edge = [[ ] for _ in range(n+1)]
for _ in range(n-1):
    fm, to = map(int,input().split())
    edge[fm].append(to)
    edge[to].append(fm)
dp = [[1, 0] for _ in range(n+1)] # [이번노드가 얼리어답터 , 이번노드는 얼리 x] 
visited = [False for _ in range(n+1)]
checkdp(1)

print(min(dp[1]))