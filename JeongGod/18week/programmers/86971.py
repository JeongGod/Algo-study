from collections import deque


def cut(cut_wires, n):
    global answer
    x, y = cut_wires
    visited = [False] * (n+1)
    visited[x] = True
    visited[y] = True
    
    answer = min(answer, abs(get_nodes(x, visited) - get_nodes(y, visited)))

def get_nodes(x, visited):
    cnt = 1
    dq = deque([x])
    while dq:
        cur = dq.popleft()
        for next in graph[cur]:
            if visited[next]:
                continue
            cnt += 1
            visited[next] = True
            dq.append(next)
    return cnt

def solution(n, wires):
    global answer, graph
    
    graph = [[] for _ in range(n+1)]
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    answer = 100
    for wire in wires:
        cut(wire, n)
    
    return answer
