import sys
input = sys.stdin.readline


def check_full(arr):
    if '.' in arr:
        return False
    return True


def count_symbol(arr):
    o_count, x_count = 0, 0
    for symbol in arr:
        if symbol == 'O':
            o_count += 1
        elif symbol == 'X':
            x_count += 1
    if o_count == x_count:
        return 'O', 'X'
    if o_count + 1 == x_count:
        return 'X', 'O'
    return False, False


def check_winner(arr, target):
    for i in range(3):
        if target == arr[i*3] == arr[i*3+1] == arr[i*3+2] or target == arr[i] == arr[i+3] == arr[i+6]:
            return True

    if target == arr[0] == arr[4] == arr[8] or target == arr[2] == arr[4] == arr[6]:
        return True

    return False


if __name__ == "__main__":
    while True:
        board = input().rstrip()

        if board == 'end':
            break

        winner, loser = count_symbol(board)
        if winner:
            if check_winner(board, winner):
                if not check_winner(board, loser):
                    print('valid')
                    continue
            else:
                if check_full(board) and not check_winner(board, loser):
                    print('valid')
                    continue

        print('invalid')
