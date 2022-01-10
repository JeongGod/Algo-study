import heapq

def solution(operations):
    answer = []
    maxq = []
    minq = []
    visited = dict()
    for command in operations:
        if command.startswith('I'):
            heapq.heappush(minq, int(command[2:]))
            heapq.heappush(maxq, -int(command[2:]))
            if (int(command[2:]) not in visited):
                visited[int(command[2:])] = 1
            else:
                visited[int(command[2:])] += 1
        else:
            if command[2] == '1':
                while maxq:
                    popvalue = -heapq.heappop(maxq)
                    if(visited[popvalue] > 0):
                        visited[popvalue] -= 1
                        break
            else:
                while minq:
                    popvalue = heapq.heappop(minq)
                    if(visited[popvalue] > 0):
                        visited[popvalue] -= 1
                        break
    while maxq:
        popvalue = -maxq[0]
        if(visited[popvalue] != 0):
            break
        else:
            heapq.heappop(maxq)
    while minq:
        popvalue = minq[0]
        if(visited[popvalue] != 0):
            break
        else:
            heapq.heappop(minq)
    if not maxq:
        return [0, 0]
    else:
        return [-maxq[0], minq[0]]