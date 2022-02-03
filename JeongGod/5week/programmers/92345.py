dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(x, y, other_x, other_y):
    global nboard
    impossible = 0
    
    # 현재 발판이 0인 경우
    if nboard[x][y] == 0:
        return False, 0
    nboard[x][y] = 0
    
    win, lose = 1e9, 0
    
    canwin = False
    
    for gx, gy in zip(dx ,dy):
        nx, ny = x + gx, y + gy
        if not(0 <= nx < len(nboard) and 0 <= ny < len(nboard[0])) or nboard[nx][ny] == 0:
            impossible += 1
            continue
        
        decision, turn = dfs(other_x, other_y, nx, ny)

        # 승패
        if not decision:
            # 해당 플레이어는 승리하는 친구다.
            canwin = True
            win = min(turn, win)
        elif not canwin:
            # 해당 플레이어는 패배하는 친구다.
            lose = max(turn, lose)
            
    nboard[x][y] = 1    
    # 상하좌우 모두 움직일 수 없는 경우
    if impossible == 4:
        # 해당 플레이어는 진다.
        return False, 0
    
    return canwin, win+1 if canwin else lose+1
    
    
def solution(board, aloc, bloc):
    global nboard
    nboard = board

    return dfs(aloc[0], aloc[1], bloc[0], bloc[1])[1]
