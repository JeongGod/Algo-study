import sys

input = sys.stdin.readline

sys.setrecursionlimit(1000000)


def dfs(graph, cur):
    global cnt, visited
    if len(graph[cur]) == 1:
        cnt += 1
        return
    for n in graph[cur]:
        if visited[n]:
            continue
        visited[n] = True
        dfs(graph, n)


def solution(graph):
    """
    1. 자식 노드를 찾는다.
    2. 자식 노드의 깊이를 안다.
    N = 50만, W = 10억
    50만에 대한 W를 구한다.
    """
    global cnt, visited
    cnt = 0
    visited = [False] * (len(graph) + 1)
    graph[1].append(0)
    visited[0] = True
    dfs(graph, 1)
    print(f"{W / cnt:07f}")


if __name__ == "__main__":
    N, W = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    solution(graph)
