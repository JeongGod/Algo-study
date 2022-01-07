from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for idx in range(n):
        if visited[idx]:
            continue
        visited[idx] = 1
        answer += 1
        dq = deque([idx])
        while dq:
            cur = dq.popleft()
            for ni in range(n):
                if visited[ni] or computers[cur][ni] != 1:
                    continue
                
                visited[ni] = 1
                dq.append(ni)
            
    return answer