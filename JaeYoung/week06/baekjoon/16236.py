from collections import deque
import sys
from typing import Deque, List, Tuple

dx: List[int] = [0, -1, 1, 0]
dy: List[int] = [1, 0, 0, -1]


def bfs(graph) -> int:
    shark_size: int = 2
    shark_feed: int = 0
    shark_time: int = 0
    answer: int = 0
    moving_que: Deque[Tuple[int, int]] = deque()
    visited: List[List[int]] = []
    init_status: int = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                moving_que.append((i, j))
                visited.append([i, j])
                graph[i][j] = 0
            init_status += graph[i][j]

    if init_status == 0:  # 물고기 한마리도 없을때
        return 0

    while moving_que:
        is_eat: bool = False

        # 위쪽 - 왼쪽 순서로 우선적으로 물고기를 먹는다고 했으니까 행, 열 순서로 오른차순 정렬
        moving_que = deque(sorted(moving_que, key=lambda x: [x[0], x[1]]))

        for _ in range(len(moving_que)):
            x, y = moving_que.popleft()

            if 0 < graph[x][y] < shark_size:  # 물고기가 상어보다 작을 때 => 상어가 냠냠
                is_eat = True
                shark_feed += 1  # 상어가 잡아먹은 물고기 횟수가 증가하고
                if shark_size == shark_feed:  # 상어의 몸집과 잡아먹은 물고기 횟수가 일치하면 상어의 몸집 크기가 1 증가!
                    shark_size += 1
                    shark_feed = 0
                graph[x][y] = 0  # 상어가 잡아먹은 물고기 자리는 0 으로

                # 상어가 물고기를 잡아먹었으면 탐색한 부분들 다시 초기화
                moving_que = deque()
                visited = [[x, y]]
                answer = shark_time

            for i in range(4):
                nx: int = x + dx[i]
                ny: int = y + dy[i]

                if 0 > nx or 0 > ny or nx >= N or ny >= N:
                    continue

                if [nx, ny] in visited:
                    continue

                if graph[nx][ny] <= shark_size:
                    moving_que.append((nx, ny))
                    visited.append([nx, ny])

            if is_eat:
                break
            
        shark_time += 1

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    graph: List[List[int]] = [
        list(map(int, input().split())) for _ in range(N)]

    print(bfs(graph))
