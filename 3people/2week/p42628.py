import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    for op in operations:
        cmd = op.split()
        n = int(cmd[1])
        if cmd[0] == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, (-n, n))
        else:
            if len(min_heap) == 0:
                pass
            elif cmd[1] == '1':
                maxx = heapq.heappop(max_heap)[1]
                min_heap.remove(maxx)
            elif cmd[1] == '-1':
                minn = heapq.heappop(min_heap)
                max_heap.remove((-minn, minn))
    if min_heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
    else:
        return [0, 0]
