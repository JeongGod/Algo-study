from collections import deque
from typing import List


def solution(bridge_length: int, weight: int, truck_weights: List[int]):
    current_weight: int = 0
    time: int = 0
    truck_que: deque = deque(truck_weights)
    bridge_que: deque = deque(maxlen=bridge_length)
    finish_truck: int = 0

    while finish_truck != len(truck_weights):
        time += 1

        if len(bridge_que) == bridge_length:
            truck = bridge_que.popleft()
            if truck != 0:
                finish_truck += 1
                current_weight -= truck

        if truck_que:
            truck = truck_que[0]
            if truck + current_weight <= weight:
                truck_que.popleft()
                bridge_que.append(truck)
                current_weight += truck
            else:
                bridge_que.append(0)
        else:
            bridge_que.append(0)

    return time


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
