from collections import deque
def removepairs(board):
    global answer
    removedpairs = set()
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if(board[i][j] != None and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]):
                removedpairs.add((i,j))
                removedpairs.add((i+1,j))
                removedpairs.add((i,j+1))
                removedpairs.add((i+1,j+1))
                
    if not removedpairs:
        return False
    answer += len(removedpairs)
    for el in removedpairs:
        board[el[0]][el[1]] = None
        
    return True    
def dropdown(board):
    for j in range(len(board[0])):
        q = deque()
        for i in range(len(board)-1 , -1, -1):
            if(board[i][j] != None):
                q.append(board[i][j])
                board[i][j] = None
        i = len(board)-1
        while q:
            board[i][j] = q.popleft()
            i -= 1

def solution(m, n, board):
    board = [[el for el in line] for line in board ]
    global answer
    answer = 0
    while True:
        if not (removepairs(board)):
            break
        dropdown(board)
        
    return answer