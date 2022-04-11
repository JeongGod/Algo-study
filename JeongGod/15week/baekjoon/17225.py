import heapq
import sys

input = sys.stdin.readline


def solution(hq : list[int, str]) -> None:
    
    pid = 1
    answer_b = []
    answer_r = []
    while hq:
        _, color = heapq.heappop(hq)
        if color == 'B':
            answer_b.append(pid)
        else:
            answer_r.append(pid)
        pid += 1

    print(len(answer_b))
    print(*answer_b)
    print(len(answer_r))
    print(*answer_r)
        


if __name__ == "__main__":
    blue_time, red_time, N = map(int, input().split())
    max_b, max_r = 0, 0
    hq = []
    for _ in range(N):
        order_time, color, cnt = input().rstrip().split()
        order_time = int(order_time)
        if color == 'B':
            t = max(order_time, max_b)
            for _ in range(int(cnt)):
                heapq.heappush(hq, (t, color))
                t += blue_time
            max_b = t
        else:
            t = max(order_time , max_r)
            for _ in range(int(cnt)):
                heapq.heappush(hq, (t, color))
                t += red_time
            max_r = t
    solution(hq)
