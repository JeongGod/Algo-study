import copy
import sys

input = sys.stdin.readline

"""
4*4 보드다. => 전체 탐색을 통해 최댓값을 얻어내자.

<물고기>
1. 물고기 번호가 작은 순으로 물고기부터 이동한다.
2. 물고기는 한 칸을 이동한다. 
3. 이동할 수 있는 칸 : 빈 칸, 다른 물고기가 있는 칸,
   이동할 수 없는 칸 : 상어가 있는 칸, 공간을 넘는 칸
4. 물고기가 다른 물고기로 갈 때에는 위치를 변경한다.

<상어>
5. 상어는 여러 칸을 이동 가능하다.
6. 그 칸에 있는 물고기를 먹고 해당 물고기의 방향을 갖는다.
"""

dist = {
    1 : (-1, 0),
    2 : (-1, -1),
    3 : (0, -1),
    4 : (1, -1),
    5 : (1, 0),
    6 : (1, 1),
    7 : (0, 1),
    8 : (-1, 1),
}

def check_move(nboard : list[list[int]], x : int, y : int, ate_fishes = set(), shark = False):
    if not (0 <= x < 4 and 0 <= y < 4):
        return False
    # 상어는 먹은 물고기라면 이동 불가능
    if shark and nboard[x][y][0] in ate_fishes:
        return False
    return True

def move_fish(nboard : list[list[int]], num : int, sx : int, sy : int):
    
    for i in range(4):
        for j in range(4):
            # 1번부터 차례대로 물고기 이동
            if nboard[i][j][0] == num and not (i == sx and j == sy):

                while True:
                    go = dist[nboard[i][j][1]]
                    nx, ny = i + go[0], j + go[1]
                    # 움직일 수 있고 그 자리에 상어가 없다면
                    if check_move(nboard, nx, ny) and not (nx == sx and ny == sy):
                        nboard[nx][ny], nboard[i][j] = nboard[i][j], nboard[nx][ny]
                        break
                    nboard[i][j][1] = (nboard[i][j][1] % 8) + 1
                return


def solution(board : list[list[int]], sx : int, sy : int, s_dist : int, ate_fishes : set[int]):
    global answer

    # 물고기가 이동한다.
    new_board = copy.deepcopy(board)
    for num in range(1, 17):
        if num in ate_fishes:
            continue
        move_fish(new_board, num, sx, sy)

    # 상어의 이동자리를 탐색한다.
    for i in range(1, 4):
        nx, ny = sx + (dist[s_dist][0] * i), sy + (dist[s_dist][1] * i)
            
        if not check_move(nboard=new_board, x=nx, y=ny, ate_fishes=ate_fishes, shark=True):
            continue
        # 물고기 먹기
        num, n_dist = new_board[nx][ny]
        ate_fishes.add(num)

        solution(new_board, nx, ny, n_dist, ate_fishes)
        ate_fishes.discard(num)
    
    # 더 이상 물고기를 먹을 수 없다면
    answer = max(answer, sum(ate_fishes))
    
    

if __name__ == "__main__":
    board = [[[0, 0] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        tmp = list(map(int, input().split()))
        for j in range(0, len(tmp), 2):
            board[i][j//2][0] = tmp[j]
            board[i][j//2][1] = tmp[j+1]
    answer = board[0][0][0]
    
    solution(board, 0, 0, board[0][0][1], {answer})
    print(answer)
