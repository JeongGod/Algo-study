import sys
from operator import add
from typing import Dict, List, Set, Tuple

WIND_DIR: Dict[int, str] = {
    1: {  # right
        "dx": [-1, 0, 1],
        "dy": [1, 1, 1],
        "onex": 0,
        "oney": 1,
        "wall_check": [
            [[0, 0, -1, 0], [-1, 0, -1, 1]],
            [[0, 0, 0, 1]],
            [[0, 0, 1, 0], [1, 0, 1, 1]]
        ]
    },
    2: {  # left
        "dx": [-1, 0, 1],
        "dy": [-1, -1, -1],
        "onex": 0,
        "oney": -1,
        "wall_check": [
            [[0, 0, -1, 0], [-1, 0, -1, -1]],
            [[0, 0, 0, -1]],
            [[0, 0, 1, 0], [1, 0, 1, -1]]
        ]
    },
    3: {  # up
        "dx": [-1, -1, -1],
        "dy": [-1, 0, 1],
        "onex": -1,
        "oney": 0,
        "wall_check": [
            [[0, 0, 0, -1], [0, -1, -1, -1]],
            [[0, 0, -1, 0]],
            [[0, 0, 0, 1], [0, 1, -1, 1]]
        ]
    },
    4: {  # down
        "dx": [1, 1, 1],
        "dy": [-1, 0, 1],
        "onex": 1,
        "oney": 0,
        "wall_check": [
            [[0, 0, 0, -1], [0, -1, 1, -1]],
            [[0, 0, 1, 0]],
            [[0, 0, 0, 1], [0, 1, 1, 1]]
        ]
    }
}

DX: List[int] = [-1, 1, 0, 0]
DY: List[int] = [0, 0, -1, 1]


def is_inside_wall(x: int, y: int) -> bool:
    return x >= 0 and y >= 0 and x < R and y < C


def is_wall_exists(x: int, y: int, px: int, py: int) -> bool:
    if (x, y, px, py) in walls:
        return True
    return False


def is_movable_kan(x: int, y: int, nx: int, ny: int, dir: int) -> bool:
    for i in range(3):
        if nx == x + WIND_DIR[dir]["dx"][i] and ny == y + WIND_DIR[dir]["dy"][i]:
            move_directions: List[List[int]] = WIND_DIR[dir]["wall_check"][i]
            for move in move_directions:
                px, py, qx, qy = list(map(add, move, [x, y, x, y]))
                if is_wall_exists(px, py, qx, qy):
                    return False
            return True


def check_temp(search_locations: List[Tuple[int, int]]) -> bool:
    for can in search_locations:
        x, y = can
        if graph[x][y] < K:
            return False
    return True


def control_temp() -> None:
    for x in range(R):
        for y in range(C):
            now_temp: int = graph[x][y]

            if now_temp == 0:
                continue

            for i in range(4):
                nx: int = x + DX[i]
                ny: int = y + DY[i]

                if not is_inside_wall(nx, ny):
                    continue

                if is_wall_exists(x, y, nx, ny):
                    continue

                near_temp: int = graph[nx][ny]

                if now_temp <= near_temp:
                    continue

                diff: int = (now_temp - near_temp)//4
                temp_adder[x][y] -= diff
                temp_adder[nx][ny] += diff

    for x in range(R):
        for y in range(C):
            temp: int = temp_adder[x][y]
            if temp == 0:
                continue
            graph[x][y] += temp


def blow_wind(x: int, y: int, temp: int, dir: int) -> None:
    graph[x][y] += temp  # 온도 올리고
    visited[x][y] = True
    for i in range(3):
        nx = x + WIND_DIR[dir]["dx"][i]
        ny = y + WIND_DIR[dir]["dy"][i]

        if not is_inside_wall(nx, ny) or visited[nx][ny]:
            continue

        # 가려는 방향에 벽이 있는지 체크
        if not is_movable_kan(x, y, nx, ny, dir):
            continue

        if temp-1 > 0:
            blow_wind(nx, ny, temp-1, dir)


if __name__ == "__main__":
    input = sys.stdin.readline
    walls: Set[Tuple[int]] = set()
    choco: int = 0
    search_locations: List[Tuple[int, int]] = []
    warmer_locations: List[Tuple[int, int]] = []
    search_flag: bool = True
    R, C, K = map(int, input().split())
    graph: List[List[int]] = [
        list(map(int, input().split())) for _ in range(R)]
    W = int(input())
    visited: List[List[bool]] = [[False] * C for _ in range(R)]

    for _ in range(W):
        x, y, d = map(int, input().split())
        if d == 1:
            walls.add((x-1, y-1, x-1, y))
            walls.add((x-1, y, x-1, y-1))
        else:
            walls.add((x-1, y-1, x-2, y-1))
            walls.add((x-2, y-1, x-1, y-1))

    for x in range(R):
        for y in range(C):
            # 온도를 조사해야하는 칸 따로 저장
            if graph[x][y] == 5:
                search_locations.append((x, y))
                # 온도를 조사해야하는 칸 0으로 바꿈
                graph[x][y] = 0

            # 온풍기 칸 위치 저장
            if 0 < graph[x][y] < 5:
                warmer_locations.append((x, y, graph[x][y]))
                # 온풍기 칸 0으로 바꿈
                graph[x][y] = 0

    # 온풍기 칸 위치 저장한 것 별로 바람 온도 조절시행
    while True:
        over_k_length: int = 0

        # 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
        for info in warmer_locations:
            x, y, dir = info
            nx = x+WIND_DIR[dir]["onex"]
            ny = y+WIND_DIR[dir]["oney"]

            blow_wind(nx, ny, 5, dir)
            visited: List[List[bool]] = [[False] * C for _ in range(R)]

        # 2. 온도가 조절됨
        temp_adder: List[List[int]] = [[0] * C for _ in range(R)]
        control_temp()

        # 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
        for x in range(R):
            if x == 0 or x == R-1:
                for y in range(C):
                    if graph[x][y] > 0:
                        graph[x][y] -= 1
            else:
                if graph[x][0] > 0:
                    graph[x][0] -= 1

                if graph[x][-1] > 0:
                    graph[x][-1] -= 1

        # 4. 초콜릿을 하나 먹는다.
        choco += 1

        if choco > 100:
            break

        # 5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.
        if check_temp(search_locations):
            break

    print(choco)
