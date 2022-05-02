import sys

input = sys.stdin.readline
answer = 0
g = int(input())
p = int(input())
parent = [i for i in range(g + 1)]
planes = []

for _ in range(p):
    planes.append(int(input()))


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


for plane in planes:
    p = find(plane)
    if p == 0:
        break
    parent[p] = parent[p - 1]
    answer += 1
print(answer)
