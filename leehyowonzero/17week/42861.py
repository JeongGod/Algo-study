# 최소 스패닝 트리 , 크루스카 알고리즘

def find(x):
    global parent
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    global parent
    rootA = find(a)
    rootB = find(b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


def solution(n, costs):
    answer = 0
    global parent
    parent = [i for i in range(n)]
    costs.sort(key = lambda x : x[2])
    for cost in costs:
        a, b , d = cost
        if find(a) != find(b):
            union(a, b)
            answer += d
            
    return answer