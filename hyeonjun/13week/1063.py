import sys
input = sys.stdin.readline

dx = {'R': 1, 'L': -1, 'B': 0, 'T': 0, 'RT': 1, 'LT': -1, 'RB': 1, 'LB': -1}
dy = {'R': 0, 'L': 0, 'B': -1, 'T': 1, 'RT': 1, 'LT': 1, 'RB': -1, 'LB': -1}

if __name__ == "__main__":
    king, pawn, n = map(str, input().split())
    orders = [str(input().rstrip()) for _ in range(int(n))]
    king_x, king_y = ord(king[0])-64, int(king[1])
    pawn_x, pawn_y = ord(pawn[0])-64, int(pawn[1])

    for order in orders:
        nx = king_x + dx[order]
        ny = king_y + dy[order]
        if nx < 1 or nx > 8 or ny < 1 or ny > 8:
            continue
        if nx == pawn_x and ny == pawn_y:
            p_nx = pawn_x + dx[order]
            p_ny = pawn_y + dy[order]
            if p_nx < 1 or p_nx > 8 or p_ny < 1 or p_ny > 8:
                continue
            king_x, king_y = nx, ny
            pawn_x, pawn_y = p_nx, p_ny
        else:
            king_x, king_y = nx, ny

    print(chr(king_x+64)+str(king_y))
    print(chr(pawn_x+64)+str(pawn_y))
