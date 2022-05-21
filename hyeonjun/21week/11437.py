import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

if __name__ == "__main__":
    def make_tree(child, parent, level):
        for node in info[child]:
            if node != parent:
                tree[node] = (child, level+1)
                make_tree(node, child, level+1)

    def find_lca(a, b):
        while True:
            a_parent, a_level = tree[a]
            b_parent, b_level = tree[b]

            if a == b:
                return a

            if a_level > b_level:
                a = a_parent
            elif b_level > a_level:
                b = b_parent
            else:
                a = a_parent
                b = b_parent

    N = int(input())
    info = [[] for _ in range(N+1)]
    tree = {i: (i, 1) for i in range(N+1)}

    for _ in range(N-1):
        u, v = map(int, input().split())
        info[u].append(v)
        info[v].append(u)

    make_tree(1, 1, 1)

    M = int(input())
    for _ in range(M):
        node1, node2 = map(int, input().split())
        print(find_lca(node1, node2))
