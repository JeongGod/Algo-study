# 1시간 풀고 정확도 20퍼 서렌
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def redmove(board, aloc, bloc, turn):
    global answer
    x, y = aloc 
    if(aloc == bloc):
        flag = False
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
                continue
            if(board[nx][ny] == 0):
                continue
            flag = True
        if(flag == False):
            answer = max(answer, turn)
            return
        answer = max(answer, turn+1)
        return 
    flag = False
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
            continue
        if(board[nx][ny] == 1  and [nx,ny] != bloc): #이동가능하면서 상대가 없는 자리
            flag = True
            board[x][y] = 0
            bluemove(board, [nx,ny], bloc, turn + 1)
            board[x][y] = 1   
        
    if(flag == False):
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if(bloc == [nx,ny]):
                board[x][y] = 0
                bluemove(board, [nx,ny], bloc, turn + 1)
                return
    if(flag == False):
        candianswer.append(turn)
    
def bluemove(board, aloc, bloc, turn):
    global answer
    x, y = bloc
    if(aloc == bloc):
        flag = False
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
                continue
            if(board[nx][ny] == 0):
                continue
            flag = True
        if(flag == False):
            answer = max(answer, turn)
            return
        answer = max(answer, turn)
        return
    flag = False
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
            continue
        if(board[nx][ny] == 1 and [nx,ny] != aloc): #이동가능하면서 상대가 없는 자리
            flag = True
            board[x][y] = 0
            redmove(board, aloc, [nx,ny], turn + 1)
            board[x][y] = 1
    
    if(flag == False):
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if(aloc == [nx,ny]):
                board[x][y] = 0
                redmove(board, aloc, [nx,ny], turn + 1)
                return
    if(flag == False):
        candianswer.append(turn)

def solution(board, aloc, bloc):
    global answer
    global candianswer
    candianswer = []
    answer = -1
    redmove(board, aloc, bloc, 0)
    if(answer == -1):
        answer = candianswer.sort()[-1]
    return answer