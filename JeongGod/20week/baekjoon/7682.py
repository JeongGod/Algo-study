import sys

"""
최종상태 판별
1. X의 개수와 O의 개수가 같을 경우
    O가 이기는 경우여야 하고 X가 이기는 경우는 없어야 한다.
2. X의 개수가 1개 많을 경우
    X가 이기는 경우거나 게임판이 가득 차 있어야 한다.
"""
input = sys.stdin.readline

def check_win(board, player):

    # 세로
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # 가로
    for i in [0, 3, 6]:
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # 대각선
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False
    

if __name__ == "__main__":
    while True:
        board = input().rstrip()
        if board == "end":
            break

        x_cnt = board.count('X')
        o_cnt = board.count('O')
        
        x_win, o_win = check_win(board, 'X'), check_win(board, 'O')

        if x_cnt == o_cnt:
            if not x_win and o_win:
                print("valid")
            else:
                print("invalid")
        elif x_cnt == o_cnt + 1:
            if x_win and not o_win:
                print("valid")
            elif x_cnt + o_cnt == 9 and not (x_win or o_win):
                print("valid")
            else:
                print("invalid")
        else:
            print("invalid")
