dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def solution(game_board, table):
    def rotate():
        tmp = []
        for elm in block_piece:
            start_x, start_y = elm[0]
            space = [(0, 0)]
            for x, y in elm[1:]:
                space.append((start_y-y, x-start_x))
            space.sort(key=lambda x: (-x[1], x[0]))
            tmp.append(space)
        return tmp

    def check_can_insert():
        cnt = 0
        for idx1, space in enumerate(empty_space):
            for idx2, piece in enumerate(block_piece):
                if filled[idx1] or used[idx2]:
                    continue

                if space == piece:
                    cnt += len(space)
                    filled[idx1] = 1
                    used[idx2] = 1
        return cnt

    def search_space(target, start_x, start_y, flag):
        space = [(0, 0)]
        stack = [(start_x, start_y)]
        target[start_x][start_y] = flag
        while stack:
            x, y = stack.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if (flag and not target[nx][ny]) or (not flag and target[nx][ny]):
                        space.append((nx-start_x, ny-start_y))
                        stack.append((nx, ny))
                        target[nx][ny] = flag
        space.sort(key=lambda x: (-x[1], x[0]))
        return space

    answer = 0
    n = len(game_board)
    empty_space = []  # 빈 공간
    block_piece = []  # 사용가능한 조각

    for x in range(n):
        for y in range(n):
            if not game_board[x][y]:
                empty_space.append(search_space(game_board, x, y, 1))
            if table[x][y]:
                block_piece.append(search_space(table, x, y, 0))

    filled = [0 for _ in range(len(empty_space))]
    used = [0 for _ in range(len(block_piece))]

    for _ in range(4):
        answer += check_can_insert()
        block_piece = rotate()

    return answer
