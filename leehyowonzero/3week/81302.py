dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x, y, dist):
    global Map
    global visited
    if dist == 2:
        return True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not (0 <= nx < 5 and 0 <= ny < 5):
            continue
        if(visited[nx][ny] == True):
            continue
        if(Map[nx][ny] == 'X'):
            continue
        if(Map[nx][ny] == 'P'):
            return False
        if(dfs(nx,ny, dist + 1) == False):
            return False
    return True
        
def CheckPlace():
    global Map
    global visited
    for i in range(5):
        for j in range(5):
            if(Map[i][j] == 'P'):
                visited[i][j] = True
                if(dfs(i,j,0) == False):
                    return 0
    return 1

def solution(places):
    global visited
    global Map
    answer = []

    for place in places:
        Map = []
        visited = [[False for _ in range(5)] for _ in range(5)]
        for col in place:
            Map.append(list(col))
        answer.append(CheckPlace())
    return answer