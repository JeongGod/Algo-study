import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

if __name__ == "__main__":
    def check(node, parent):
        for child in tree[node]:
            if child != parent:
                check(child, node)
                dp[node][0] += dp[child][1]
                dp[node][1] += min(dp[child][0], dp[child][1])

    N = int(input())
    tree = [[] for _ in range(N+1)]

    for _ in range(N-1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    dp = [[0, 1] for _ in range(N+1)]

    check(1, 1)
    print(min(dp[1]))
