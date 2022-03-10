from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
# 가상자리만 검사해서 진짜 "O" 집합을 걸러줬습니다.
class Solution: 
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in ([0, len(board)-1]): # 맨 위, 아래 행
            for j in range(len(board[0])):
                if(board[i][j] == 'O'):
                    q = deque()
                    q.append([i, j])
                    board[i][j] = "REALO"
                    while q:
                        x, y = q.popleft()
                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
                                continue
                            if(board[nx][ny] == 'O'):
                                board[nx][ny] = "REALO"
                                q.append([nx,ny])
                                
        for i in range(len(board)): # 맨 왼쪽, 오른족 열
            for j in ([0, len(board[0]) -1]):
                if(board[i][j] == 'O'):
                    q = deque()
                    q.append([i, j])
                    board[i][j] = "REALO"
                    while q:
                        x, y = q.popleft()
                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
                                continue
                            if(board[nx][ny] == 'O'):
                                board[nx][ny] = "REALO"
                                q.append([nx,ny])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == "O"):
                    board[i][j] = "X"
                elif(board[i][j] == "REALO"):
                    board[i][j] = "O"
                