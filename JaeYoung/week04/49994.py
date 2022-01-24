from typing import List, Set

def solution(dirs): 
    visited: Set = set()
    x, y = [0, 0]
    direction: dict = {
        "U": [0, 1],
        "D": [0, -1],
        "L": [-1, 0],
        "R": [1, 0]
    }
    
    for dir in dirs:  
        adder = direction[dir]
        nx, ny = [x + adder[0], y + adder[1]]
        
        if abs(nx) > 5 or abs(ny) > 5:
            continue

        x_move: List[int] = [x, nx]
        y_move: List[int] = [y, ny]
        x_move.sort()
        y_move.sort()
        move_path: List[int] = x_move + y_move
        visited.add(tuple(move_path))
        x, y = [nx, ny]
        
    answer = len(visited)
    return answer