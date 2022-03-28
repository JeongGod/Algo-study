import sys

input = sys.stdin.readline

dist = {
    "R" : (0, 1),
    "L" : (0, -1),
    "B" : (-1, 0),
    "T" : (1, 0),
    "RT" : (1, 1),
    "LT" : (1, -1),
    "RB" : (-1, 1),
    "LB" : (-1, -1)
}

def check(x, y):
    return 1 <= x <= 8 and ord('A') <= y <= ord('H')

def solution(king : str, stone : str, moves : list[str]):
    # king[0] = 열, king[1] = 행
    kx, ky = int(king[1]), ord(king[0])
    stx, sty = int(stone[1]), ord(stone[0])
    for m in moves:
        nx, ny = kx + dist[m][0], ky + dist[m][1]
        # 이동이 불가능하다면
        if not check(nx, ny):
            continue
        if stx == nx and sty == ny:
            nstx, nsty = nx + dist[m][0], ny + dist[m][1]
            if not check(nstx, nsty):
                continue
            stx, sty = nstx, nsty
        kx, ky = nx, ny
    
    print(chr(ky)+str(kx))
    print(chr(sty)+str(stx))

if __name__ == "__main__":
    king, stone, move_cnt = input().rstrip().split()
    moves = [input().rstrip() for _ in range(int(move_cnt))]
    solution(king, stone, moves)
