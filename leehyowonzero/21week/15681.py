import sys
sys.setrecursionlimit(100000)

def calcnode(root):
    if(node[root] == 0):
        node[root] += 1
    for el in edge[root]:
        if(node[el] == 0):
            calcnode(el)
            node[root] += node[el]

n, r, q = map(int,input().split())
edge = [[] for _ in range(n+1)]
for _ in range(n-1):
    fm, to = map(int,input().split())
    edge[fm].append(to)
    edge[to].append(fm)
node = [0 for _ in range(n+1)]
calcnode(r)


for _ in range(q):
    x = int(input())
    print(node[x])