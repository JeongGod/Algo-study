import heapq
import sys

input = sys.stdin.readline


def solution(n: int, m: int, abilities: list[list[int]]) -> int:
    answer = sys.maxsize
    hq = []
    max_val = 0
    # 최솟값을 갖고 있는 우큐를 만든다.
    for i in range(n):
        heapq.heappush(hq, (abilities[i][0], i, 0))
        max_val = max(max_val, abilities[i][0])

    while True:
        # 최대 최소 값을 비교한다.
        min_val, h, w = heapq.heappop(hq)
        if max_val - min_val < answer:
            answer = max_val - min_val
        # 해당 최솟값에 해당하는 친구를 한 칸 땡긴다.
        # 땡길 수 없다면 끝이 난다.
        if w == m - 1:
            return answer
        # 최댓값을 교체해야하는지 살펴본다.
        if max_val < abilities[h][w + 1]:
            max_val = abilities[h][w + 1]
        heapq.heappush(hq, (abilities[h][w + 1], h, w + 1))


if __name__ == "__main__":
    N, M = map(int, input().split())
    abilities = [sorted(list(map(int, input().split()))) for _ in range(N)]
    print(solution(N, M, abilities))
