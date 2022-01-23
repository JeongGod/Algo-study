from collections import deque


def rotate(x1, y1, x2, y2, matrix):
    queue = deque()
    for i in range(y1-1, y2-1, 1):
        queue.append(matrix[x1-1][i])
    for i in range(x1-1, x2-1, 1):
        queue.append(matrix[i][y2-1])
    for i in range(y2-1, y1-1, -1):
        queue.append(matrix[x2-1][i])
    for i in range(x2-1, x1-1, -1):
        queue.append(matrix[i][y1-1])

    tmp = min(queue)
    for i in range(y1, y2, 1):
        matrix[x1-1][i] = queue.popleft()
    for i in range(x1, x2, 1):
        matrix[i][y2-1] = queue.popleft()
    for i in range(y2-2, y1-2, -1):
        matrix[x2-1][i] = queue.popleft()
    for i in range(x2-2, x1-2, -1):
        matrix[i][y1-1] = queue.popleft()
    return tmp


def solution(rows, columns, queries):
    answer = []
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append((i)*columns+j+1)

    for query in queries:
        answer.append(rotate(query[0], query[1], query[2], query[3], matrix))

    return answer
