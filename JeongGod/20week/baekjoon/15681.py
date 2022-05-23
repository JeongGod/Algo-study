import sys

sys.setrecursionlimit(100002)
input = sys.stdin.readline


def dfs(cur):
    global answer

    visited[cur] = True
    for ncur in tree[cur]:
        if visited[ncur]:
            continue
        answer[cur] += dfs(ncur)

    # 리프노드라면
    if answer[cur] == 0:
        return 1
    return answer[cur] + 1

if __name__ == "__main__":
    N, R, Q = map(int, input().split())

    tree = [[] for _ in range(N+1)]
    answer = [0] * (N+1)
    visited = [False] * (N+1)
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    result = [int(input()) for _ in range(Q)]

    dfs(R)
    for i in result:
        print(answer[i] + 1)
