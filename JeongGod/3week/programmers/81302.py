from collections import deque
def solution(places):
    """
    회의실 5개, 5*5
    2이하로 앉지 말아야한다. 3이상이여야 한다.
    파티션으로 막혀있을 경우에는 허용한다.
    
    1. 벽이 있으면 진행 X
    2. 진행하다가 사람을 만나면 False
    """
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    def bfs(x, y, board):
        dq = deque([(x, y, 0)])
        visited = {(x, y)}
        while dq:
            cx, cy, cnt = dq.popleft()
            if cnt == 2:
                continue
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5:
                    # 벽을 만나거나 방문한 곳이라면
                    if board[nx][ny] == "X" or (nx, ny) in visited:
                        continue
                    # 사람을 만났다면
                    if board[nx][ny] == "P":
                        return False
                    visited.add((nx, ny))
                    dq.append((nx, ny, cnt+1))
        return True
    
    def check(place):
        for room_idx in range(5):
            for idx in range(5):
                # 사람인 곳을 찾아 거리두기가 되었는지 체크한다.
                if place[room_idx][idx] == "P":
                    if not bfs(room_idx, idx, place):
                        return False
        return True
            
    answer = []        
    
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer