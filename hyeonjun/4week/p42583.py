from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0 for _ in range(bridge_length)])
    now_weight = 0
    while queue:
        answer += 1
        now_weight -= queue.popleft()
        if truck_weights:
            if now_weight + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                queue.append(truck)
                now_weight += truck
            else:
                queue.append(0)
    return answer
