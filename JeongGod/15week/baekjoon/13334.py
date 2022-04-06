import heapq
import sys

input = sys.stdin.readline


def solution(people : list[tuple[int, int]], end_people : list[tuple[int, int]], bridge : int) -> int:
    """
    1. people을 시작점으로 정렬한다.
    2. 해당 끝 점을 기준을 잡고 우선순위큐에서 가능한 녀석들을 뽑는다.
        끝 점이 다리 끝점보다 작으면 가능
    3. 그 다음에 해당 개수를 answer과 비교한다.
    4. 그리고 현재 개수에서 - 1 을 하여 현재 다리는 제외하고 그 다음 다리에서 1번을 반복한다.
    """
    answer = 0
    cnt = 0
    for start, _ in people:
        
        bridge_end = start + bridge

        while end_people:
            end, start1 = heapq.heappop(end_people)
            if bridge_end >= end:
                cnt += 1
            else:
                heapq.heappush(end_people, (end, start1))
                break
        answer = max(answer, cnt)
        cnt -= 1
    return answer

if __name__ == "__main__":
    N = int(input())
    people = []
    end_people = []
    for _ in range(N):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        people.append((a, b))
        end_people.append((b, a))
    bridge = int(input())

    people = list(filter(lambda x: x[1] - x[0] <= bridge, people))
    end_people = list(filter(lambda x: x[0] - x[1] <= bridge, end_people))
    heapq.heapify(end_people)

    people.sort(key=lambda x: x[0])

    print(solution(people, end_people, bridge))
