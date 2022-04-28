import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)


def get_parent(node):
    if parent[node] == node:
        return node
    return get_parent(parent[node])


if __name__ == "__main__":
    ans = 0
    n, m = map(int, input().split())
    parent = [i for i in range(n)]

    for rnd in range(m):
        dot1, dot2 = map(int, input().split())
        parent1, parent2 = get_parent(dot1), get_parent(dot2)

        if parent1 == parent2:
            ans = rnd + 1
            break

        if parent1 < parent2:
            parent[parent2] = parent1
        else:
            parent[parent1] = parent2

    print(ans)
