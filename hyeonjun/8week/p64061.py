def solution(board, moves):
    answer = 0
    stack = []
    length = len(board)

    for move in moves:
        catched_doll = 0
        for i in range(length):
            if board[i][move-1]:
                catched_doll = board[i][move-1]
                board[i][move-1] = 0
                break

        if catched_doll:
            if stack and stack[-1] == catched_doll:
                stack.pop()
                answer += 2
            else:
                stack.append(catched_doll)

    return answer
