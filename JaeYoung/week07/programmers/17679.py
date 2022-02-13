from typing import List, Tuple, Set

dcol = [1, 0, 1]
drow = [0, 1, 1]


def is_inrange(row, col) -> bool:
    if 0 <= row < rsize and 0 <= col < csize:
        return True

    return False


def is_four_block(row, col) -> List[Tuple[int]]:
    """
    4개 모두 같은 블록이면 블록의 위치 리스트 반환
    같은 블록들이 아니거나 범위를 블록 개수가 4개가 안되면 빈 리스트 반환
    """
    block_location: List[Tuple[int, int]] = []

    # 처음 블록 종류 확인
    first_block: str = gboard[row][col]
    block_location.append((row, col))
    for i in range(3):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        if is_inrange(nrow, ncol) is False:
            return []

        if gboard[nrow][ncol] != first_block:
            return []

        block_location.append((nrow, ncol))

    return block_location


def check_blocks() -> Set[Tuple[int, int]]:
    """
    지워지는 블록들의 좌표를 구해 set 으로 반환
    """
    blocks: Set[Tuple[int, int]] = set()
    for i in range(rsize):
        for j in range(csize):
            if gboard[i][j] == "X":
                continue
            result: List[Tuple[int, int]] = is_four_block(i, j)
            for ele in result:
                blocks.add(ele)

    return blocks


def delete_blocks(delete_positions: Set[Tuple[int, int]]):
    for pos in delete_positions:
        row, col = pos
        gboard[row][col] = "X"


def arrange_blocks() -> None:
    for col in range(csize):
        for row in range(rsize-1, 0, -1):
            if gboard[row][col] == "X":
                for xrow in range(row-1, -1, -1):
                    if gboard[xrow][col] != "X":
                        tmp = gboard[xrow][col]
                        gboard[row][col] = tmp
                        gboard[xrow][col] = "X"
                        break


def solution(m: int, n: int, board: List[str]):
    global gboard, rsize, csize
    answer: int = 0
    gboard = [list(row) for row in board]
    rsize = m
    csize = n
    four_blocks: List[Set[Tuple[int, int]]] = []

    while True:
        result: Set[Tuple[int, int]] = check_blocks()

        if len(result) == 0:
            break

        four_blocks.append(result)
        delete_blocks(result)
        arrange_blocks()

    for x in four_blocks:
        answer += len(x)

    return answer

# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
