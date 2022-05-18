import sys
input = sys.stdin.readline
sys.setrecursionlimit(100002)

if __name__ == '__main__':
    def count_subtree(u):
        size[u] = 1
        for node in edge[u]:
            if not size[node]:
                count_subtree(node)
                size[u] += size[node]

    N, R, Q = map(int, input().split())
    edge = [[] for _ in range(N+1)]
    size = [0 for _ in range(N+1)]

    for _ in range(N-1):
        U, V = map(int, input().split())
        edge[U].append(V)
        edge[V].append(U)

    count_subtree(R)

    for _ in range(Q):
        print(size[int(input())])
