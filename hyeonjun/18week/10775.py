import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


if __name__ == "__main__":
    g = int(input())
    p = int(input())
    airplanes = [int(input().rstrip()) for _ in range(p)]
    parent = {i: i for i in range(0, g+1)}
    count = 0

    for airplane in airplanes:
        x = find(airplane)
        if not x:
            break
        parent[x] = parent[x-1]
        count += 1

    print(count)
