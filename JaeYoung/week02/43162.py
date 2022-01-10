from collections import deque

def bfs(start, computers, visited):
    que = deque([start])
    visited[start] = True

    while que:
        v = que.popleft()
        visited[v] = True
        for i in range(len(computers[v])):
            if computers[v][i] == 1 and visited[i] == False: #컴퓨터와 연결되어있고 방문하지 않은 컴퓨터의 경우
                que.append(i)
    return visited

    
def solution(n, computers):
    visited = [False] * n # 방문한 컴퓨터 리스트
    answer = 0
            
    while False in visited: # 모든 컴퓨터를 방문할 때까지
        start = visited.index(False) #방문하지 않은 컴퓨터를 선택
        answer += 1 #네트워크 추가
        visited = bfs(start, computers, visited) #bfs를 통해 컴퓨터와 연결된 다른 컴퓨터 방문을 통해 방문 리스트 갱신
    
    return answer