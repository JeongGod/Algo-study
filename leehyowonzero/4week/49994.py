# 2차원 좌표계를 1차원으로 변환하여 각 좌표 사이의 방문을 의미하느 2차원 visited 배열을 만들어 풀이
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def solution(dirs):
    answer = 0
    visited = [[False for _ in range(121)] for _ in range(121)]
    x , y = 5, 5 #(-5,-5)를 (0, 0)으로 치환하면 좌표상 시작지점 (0,0) => (5,5) 1차원 배열 값으로 치환 => 5 + 5*11= 60
    Onedimension = 60
    for el in dirs:
        if el == "U":
            nx = x + dx[0]
            ny = y + dy[0]
            if not (0 <= nx <= 10 and 0 <= ny <= 10):
                continue
            nextOnedimension = nx + ny*11
            if(visited[Onedimension][nextOnedimension] == False):
                visited[Onedimension][nextOnedimension] = True
                visited[nextOnedimension][Onedimension] = True
                answer += 1
            x, y, Onedimension = nx, ny, nextOnedimension
                
        elif el == "R":
            nx = x + dx[1]
            ny = y + dy[1]
            if not (0 <= nx <= 10 and 0 <= ny <= 10):
                continue
            nextOnedimension = nx + ny*11
            if(visited[Onedimension][nextOnedimension] == False):
                visited[Onedimension][nextOnedimension] = True
                visited[nextOnedimension][Onedimension] = True
                answer += 1
            x, y, Onedimension = nx, ny, nextOnedimension
        elif el == "D":
            nx = x + dx[2]
            ny = y + dy[2]
            if not (0 <= nx <= 10 and 0 <= ny <= 10):
                continue
            nextOnedimension = nx + ny*11
            if(visited[Onedimension][nextOnedimension] == False):
                visited[Onedimension][nextOnedimension] = True
                visited[nextOnedimension][Onedimension] = True
                answer += 1
            x, y, Onedimension = nx, ny, nextOnedimension
        elif el == "L":
            nx = x + dx[3]
            ny = y + dy[3]
            if not (0 <= nx <= 10 and 0 <= ny <= 10):
                continue
            nextOnedimension = nx + ny*11
            if(visited[Onedimension][nextOnedimension] == False):
                visited[Onedimension][nextOnedimension] = True
                visited[nextOnedimension][Onedimension] = True
                answer += 1
            x, y, Onedimension = nx, ny, nextOnedimension
    return answer

