import math
import sys
from collections import deque

input = sys.stdin.readline

def lca(a, b):
    global rank
    # 깊이를 같게 만든다.
    while rank[a] != rank[b]:
        a = dp[a][int(math.log2(rank[a] - rank[b]))]
    
    if a == b:
        return a

    # 공통 부모를 찾는다.
    for i in range(LEN-1, -1, -1):
        if dp[a][i] != dp[b][i]:
            a = dp[a][i]
            b = dp[b][i]
    return dp[a][0]

if __name__ == "__main__":
    N = int(input())
    tree = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    rank = [0] * (N+1)
    LEN = int(math.log2(N))+1
    dp = [[0] * LEN for _ in range(N+1)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    # 트리 탐색
    dq = deque([1])
    visited[1] = True
    depth = 0
    while dq:
        depth += 1
        for _ in range(len(dq)):
            cur = dq.popleft()
            for ncur in tree[cur]:
                if visited[ncur]:
                    continue
                visited[ncur] = True
                dp[ncur][0] = cur
                rank[ncur] = depth
                dq.append((ncur))
    # 부모 갱신
    for i in range(1, LEN):
        for cur in range(1, N+1):
            dp[cur][i] = dp[dp[cur][i-1]][i-1]
    
    # 부모를 이분탐색으로 찾는다.
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        # 차이를 제곱수만큼 이동하며 좁힌다.
        if rank[a] > rank[b]:
            print(lca(a, b))
        else:
            print(lca(b, a))
