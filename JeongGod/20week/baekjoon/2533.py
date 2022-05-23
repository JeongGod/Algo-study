import sys

sys.setrecursionlimit(1000001)
input = sys.stdin.readline

def dfs(cur):
    global visited, dp
    visited[cur] = True
    
    for ncur in tree[cur]:
        if visited[ncur]:
            continue
        result = dfs(ncur)
        
        ali, notali = result
        dp[cur][0] += min(ali, notali)
        dp[cur][1] += ali
    # 얼리어답터인 경우, 얼리어답터가 아닌 경우
    # 리프노드인 경우
    if dp[cur][0] == 0 and dp[cur][1] == 0:
        return (1, 0)

    dp[cur][0] += 1
    return dp[cur]


if __name__ == "__main__":
    """
    1. 내가 얼리어답터인 경우
        자식 노드 중 (얼리어답터인 경우, 얼리어답터가 아닌 경우)중 작은 값
    2. 내가 얼리어답터가 아닌 경우
        자식 노드의 얼리어답터인 경우를 더한다.
    """
    N = int(input())
    
    tree = [[] for _ in range(N+1)]

    visited = [False] * (N+1)
    dp = [[0, 0] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    print(min(dfs(1)))
