import heapq

def solution(operations):
    max_que = []
    min_que = []
    
    for op in operations:
        if "I" in op:
            num = int(op[2:])
            heapq.heappush(min_que, num)
            heapq.heappush(max_que, -1 * num)

        elif "D" in op:
            command = int(op[2:])
            if command == 1 and len(max_que): #큐에서 최댓값 삭제
                x = heapq.heappop(max_que)
                min_que.remove(-1 * x)
            
            elif command == -1 and len(min_que): #큐에서 최솟값 삭제
                x = heapq.heappop(min_que)
                max_que.remove(-1 * x)

    if len(min_que) == 0:
        return [0, 0]
    
    return [max_que[0] * -1, min_que[0]]