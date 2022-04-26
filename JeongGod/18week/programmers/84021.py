from collections import defaultdict, deque

R, C = 0, 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check(x, y):
    return 0 <= x < R and 0 <= y < C



def search_puzzle(x, y, board, visited):
    dq = deque([(x, y)])
    visited[x][y] = True
    puzzles = [(0, 0)]
    
    while dq:
        cx, cy = dq.popleft()
        
        for gx, gy in zip(dx, dy):
            nx, ny = cx + gx, cy + gy
            if not check(nx, ny) or visited[nx][ny]:
                continue
            if board[nx][ny] != board[x][y]:
                continue
            visited[nx][ny] = True
            puzzles.append((nx-x, ny-y))
            dq.append((nx, ny))
    return puzzles

def section_puzzle(table, x, y, section, visited):
    for ax, ay in search_puzzle(x, y, table, visited):
        table[x+ax][y+ay] = section

def make_puzzle(puzzles, table):
    visited = [[False] * C for _ in range(C)]
    for x in range(R):
        for y in range(C):
            if visited[x][y] or table[x][y] == 0:
                continue
            puzzles[table[x][y]].add(tuple(search_puzzle(x, y, table, visited)))

def rotate(table):
    result = []
    for y in range(C):
        tmp = []
        for x in range(R-1, -1, -1):
            tmp.append(table[x][y])
        result.append(tmp)
    return result

def check_puzzle(puzzles, puzzle_pos):
    for key, values in puzzles.items():
        for val in values:
            if val == tuple(puzzle_pos):
                del puzzles[key]
                return len(val)
    return 0

def solution(game_board, table):
    global R,C
    answer = 0
    
    R = len(game_board)
    C = len(game_board[0])
    
    puzzles = defaultdict(set)
    
    section = 1
    tmp_visited = [[False] * C for _ in range(C)]
    for x in range(R):
        for y in range(C):
            if table[x][y] == 0 or tmp_visited[x][y]:
                continue
            section_puzzle(table, x, y, section, tmp_visited)
            section += 1
    
    
    for _ in range(4):
        make_puzzle(puzzles, table)
        table = rotate(table)
    
    
    game_visited = [[False] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if game_board[x][y] == 1 or game_visited[x][y]:
                continue
            answer += check_puzzle(puzzles, search_puzzle(x, y, game_board, game_visited))
    
    return answer
