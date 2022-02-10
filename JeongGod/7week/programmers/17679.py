from typing import List, Set, Tuple

dist = [(0, 1), (1, 0), (1, 1)]



def check_blocks(x : int, y : int, board : List[str]) -> bool:
    
    def check(x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
    
    for gx, gy in dist:
        nx, ny = x + gx, y + gy
        if not check(nx, ny) or board[nx][ny] != board[x][y] or board[x][y] == "0":
            return False

    return True

def delete_blocks(blocks : Set[Tuple[int]], board : List[str]) -> None:
    for i, j in blocks:
        board[i][j] = "0"

def down_blocks(m : int, n : int, board : List[str]) -> None:
    for j in range(n):
        st = []
        for i in range(m):
            if board[i][j] == "0":
                continue
            st.append(board[i][j])
            board[i][j] = "0"
        level = m-1
        while st:
            board[level][j] = st.pop()
            level -= 1

def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    for _ in range(10):
        blocks = set()
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "0":
                    continue
                # 4개의 블록이 되는지 체크
                if not check_blocks(i, j, board):
                    continue
                blocks.add((i, j))
                
                for gx, gy in dist:
                    blocks.add((i + gx, j + gy))

        
        answer += len(blocks)
        # 더 지울 블록이 없다면
        if not blocks:
            return answer

        # 블록을 지운다.
        delete_blocks(blocks, board)
        # 블록을 내린다.
        down_blocks(m, n, board)

print(solution(4,5, [
    "AAAAA","AUUUA","AUUAA","AAAAA"]))
