def solution(board, moves): # 옛날풀이네요
    answer = 0
    n = len(board)
    arr = []
    for i in moves:
        for j in range(0,n):
            if board[j][i-1]:
                arr.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(arr) > 1:
            if(arr[-1] == arr[-2]):
                arr.pop()
                arr.pop()
                answer += 2
    return answer