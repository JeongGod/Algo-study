from typing import List


board: List[List[int]]


def turn(x1: int, y1: int, x2: int, y2: int) -> int:
    value: int = board[x1][y1]
    min_value: int = value

    for ridx in range(x1, x2):
        board[ridx][y1] = board[ridx + 1][y1]
        min_value = min(min_value, board[ridx][y1])

    for cidx in range(y1, y2):
        board[x2][cidx] = board[x2][cidx + 1]
        min_value = min(min_value, board[x2][cidx])

    for ridx in range(x2, x1, -1):
        board[ridx][y2] = board[ridx - 1][y2]
        min_value = min(min_value, board[ridx][y2])

    for cidx in range(y2, y1, -1):
        board[x1][cidx] = board[x1][cidx - 1]
        min_value = min(min_value, board[x1][cidx])

    board[x1][y1 + 1] = value

    return min_value


def solution(rows: int, columns: int, queries: List[List[int]]) -> List[int]:
    global board
    board = [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]

    return [turn(x1 - 1, y1 - 1, x2 - 1, y2 - 1) for x1, y1, x2, y2 in queries]


# [8, 10, 25]
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
# [1, 1, 5, 3]
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
# [1]
print(solution(100, 97, [[1, 1, 100, 97]]))
