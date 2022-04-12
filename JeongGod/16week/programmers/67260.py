import sys
from collections import deque

sys.setrecursionlimit(10000000)

def go(node):
    a = True
    b = check.get(node)
    # 일반 노드일 경우
    if b is None:
        if visited[node]:
            return True
        return go(parent[node])
    else:
        # 순환일 경우
        if b[0]:
            return False
        if b[1]:
            return go(parent[node])
        # 순환 체크
        b[0] = True
        b[1] = True
        result = go(parent[node]) & go(b[2])
        b[0] = False
        return result


def dfs(graph, cur):
    global answer
    if not answer:
        return
    # 막혀있는 노드라면 뚫어주러 간다.
    blocked = check.get(cur)
    if blocked is not None:
        result = go(cur)
        # 만약 뚫는데 실패했다면
        if not result:
            answer = False
            return
    
    # 계속해서 dfs탐색을 진행한다.
    for node in graph[cur]:
        if visited[node]:
            continue
        visited[node] = True
        dfs(graph, node)
    
def solution(n, path, order):
    global check, answer, visited, parent
    answer = True
    graph = [[] for _ in range(n)]
    for x, y in path:
        graph[x].append(y)
        graph[y].append(x)
    
    check = dict()
    for x, y in order:
        check[y] = [False, False, x]
    
    parent = [0] * n
    tmp = [False] * n
    tmp[0] = True
    
    dq = deque([(0, 0)])
    while dq:
        p, cur = dq.popleft()
        parent[cur] = p
        for ne in graph[cur]:
            if tmp[ne]:
                continue
            tmp[ne] = True
            dq.append((cur, ne))
    
    visited = [False] * n
    visited[0] = True
    dfs(graph, 0)
    return answer
