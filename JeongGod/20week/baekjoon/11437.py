import math
import sys
from collections import deque

input = sys.stdin.readline

def lca(a, b):
    global rank
    # 깊이를 같게 만든다.
    while rank[a] != rank[b]:
        a = dp[a][int(math.log2(rank[a] - rank[b]))]
    
    # 공통 부모를 찾는다.
    depth = rank[a]
    while a != b:
        cnt = int(math.log2(depth))
        while True:
            tmp_a = dp[a][cnt]
            tmp_b = dp[b][cnt]
            if tmp_a != tmp_b or cnt == 0:
                break
            cnt //= 2
        a = tmp_a
        b = tmp_b
    return a
if __name__ == "__main__":
    N = int(input())
    tree = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    rank = [0] * (N+1)
    dp = [[0] * (int(math.log2(N))+1) for _ in range(N+1)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    dq = deque([(0, 1)])
    visited[1] = True
    depth = 0
    while dq:
        depth += 1
        for _ in range(len(dq)):
            parent, cur = dq.popleft()
            dp[cur][0] = parent
            for i in range(1, int(math.log2(depth)) + 1):
                dp[cur][i] = dp[dp[cur][i-1]][i-1]
            for ncur in tree[cur]:
                if visited[ncur]:
                    continue
                visited[ncur] = True
                rank[ncur] = depth
                dq.append((cur, ncur))
    
    # 부모를 이분탐색으로 찾는다.
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        # 차이를 제곱수만큼 이동하며 좁힌다.
        if rank[a] > rank[b]:
            print(lca(a, b))
        else:
            print(lca(b, a))
