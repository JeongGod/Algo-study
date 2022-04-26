block_1 = [(1, 0), (1, 1), (1, 2), (0, 1), (0, 2)]
block_2 = [(1, -2), (1, -1), (1, 0), (0, -1), (0, -2)]
block_3 = [(1, 0), (2, 0), (2, 1), (0, 1), (1, 1)]
block_4 = [(1, 0), (2, -1), (2, 0), (0, -1), (1, -1)]
block_5 = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
blocks = [block_1] + [block_2] + [block_3] + [block_4] + [block_5]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

answer = 0


def solution(board):
    def check_shape(arr):
        arr.sort(reverse=True)
        if arr[0][0] == arr[1][0]:
            shape = []
            top_x, top_y = arr[-1]
            for x, y in arr[:3]:
                shape.append((x-top_x, y-top_y))
            for block in blocks:
                if set(shape) == set(block[:3]):
                    return block, arr[-1][0], arr[-1][1]
        return 0, 0, 0

    def check_can_del(start_x, start_y, block_num):
        stack = [(start_x, start_y)]
        block_positions = [(start_x, start_y)]
        while stack:
            x, y = stack.pop()
            board[x][y] *= -1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == block_num:
                    stack.append((nx, ny))
                    block_positions.append((nx, ny))
        return check_shape(block_positions)

    def check_can_add_black(x, y, arr):
        for dx, dy in arr:
            target_x, target_y = x + dx, y+dy
            for i in range(target_x+1):
                if not board[i][target_y]:
                    continue
                if board[i][target_y] < 0 or not go(i, target_y):
                    return False
        return True

    def del_block(x, y, arr):
        board[x][y] = 0
        for dx, dy in arr:
            board[x+dx][y+dy] = 0
        return 0

    def go(x, y):
        global answer
        target, x, y = check_can_del(x, y, board[x][y])
        if target and check_can_add_black(x, y, target[3:]):
            del_block(x, y, target[:3])
            answer += 1
            return True
        return False

    N = len(board)
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0:
                go(x, y)

    return answer
