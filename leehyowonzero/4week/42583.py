from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    BridgeState = deque([0 for _ in range(bridge_length)])
    BridgeWeight = 0
    while truck_weights:
        answer += 1
        BridgeState.rotate(1)
        BridgeWeight -= BridgeState[-1]
        if(BridgeWeight + truck_weights[0] <= weight):
            BridgeState[-1] = truck_weights[0]
            BridgeWeight += truck_weights[0]
            truck_weights = truck_weights[1:]
        else:
            BridgeState[-1] = 0   
            
    for i in range(bridge_length-1, -1 ,-1):
        if(BridgeState[i] != 0):
            answer += i + 1
            break
            
    return answer