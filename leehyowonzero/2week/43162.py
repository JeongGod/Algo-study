def dfs(start, computers, n):
    visited[start] = 1
    for i in range(0,n):
        if(computers[start][i] == 1 and visited[i] == 0):
            dfs(i, computers, n)
            
def solution(n, computers):
    global visited
    answer = 0
    visited = [0 for _ in range(n)] # 0 ~ n-1 idx 컴퓨터에 방문 처리
    for i in range(n):
        if(visited[i] == 0):
            dfs(i, computers, n)
            answer += 1
    return answer