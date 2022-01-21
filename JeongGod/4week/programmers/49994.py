def check(x, y):
    if 0 <= x <= 10 and 0 <= y <= 10:
        return True
    return False
def solution(dirs):
    answer = 0
    # 한 점에서 4방향의 길을 탐색
    visited = [[[False, False, False, False] for _ in range(11)] for _ in range(11)]
    dist = {"U" : (0, 3, [1, 0]), "L" : (1, 2, [0, -1]), "R" : (2, 1, [0, 1]), "D" : (3, 0, [-1, 0])}
    
    cur = [5, 5]
    
    for go in dirs:
        direct, reverse_direct, [gx, gy] = dist[go]
        nx, ny = cur[0] + gx, cur[1] + gy
        # 보드 안에 있는지 체크
        if not check(nx, ny):
            continue
        # 방문했던 적이 있더라면
        if visited[cur[0]][cur[1]][direct]:
            # 위치 변경
            cur = [nx, ny]
            continue
        # 방문 처리 및 거리 갱신
        visited[cur[0]][cur[1]][direct] = True
        visited[nx][ny][reverse_direct] = True

        # 위치 변경
        cur = [nx, ny]
        
        answer += 1
        
    
    return answer
