from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    """
    truck_weights의 순서대로 트럭이 지나간다.
    bridge_length만큼 트럭이 들어간다. => 이게 곧 다리의 길이
    weight만큼 무게를 견딘다.
    bridge_length초 : 다리 건넘
    """
    bridge = deque([])
    idx = 0
    cur_weight = 0
    while idx < len(truck_weights):
        answer += 1
        # 다리 맨 앞에 있는 트럭이 다 건넜는지 확인
        if bridge and bridge[0][0] - answer == 0:
            _, t_weight = bridge.popleft()
            cur_weight -= t_weight
        
        # 무게를 견딜 수 있다면
        if weight >= cur_weight + truck_weights[idx]:
            # 무게 조정
            cur_weight += truck_weights[idx]
            # 다리에 트럭을 올린다. (걸리는 시간, 해당 트럭의 무게)
            bridge.append((answer + bridge_length, truck_weights[idx]))
            idx += 1
    # 트럭을 다리에 다 올렸다면 맨 마지막에 있는 트럭의 시간이 곧 정답
    return bridge[-1][0]
