from heapq import heappush, heappop


def pop(target_heap, remain_heap):
    while target_heap:
        target = -heappop(target_heap)
        if target in remain_heap:
            return target
    return 0


def solution(operations):
    min_heap = []
    max_heap = []
    for operation in operations:
        command, number = operation.split()
        number = int(number)
        if command == "I":
            heappush(min_heap, number)
            heappush(max_heap, (-number))
        elif number == 1:
            pop(max_heap, min_heap)
        else:
            pop(min_heap, max_heap)

    max_value = pop(max_heap, min_heap)
    min_value = -pop(min_heap, max_heap)

    return [max_value, min_value]
