from heapq import heappop, heappush
from typing import List, Set, Tuple


maxheap: List[Tuple[int, int]] = []
minheap: List[Tuple[int, int]] = []
removed: Set[int] = set()


def insert(data: int, idx: int) -> None:
    heappush(maxheap, (-data, idx))
    heappush(minheap, (data, idx))


def delete(heap: List[Tuple[int, int]]) -> None:
    while heap:
        _, idx = heappop(heap)
        if idx not in removed:
            removed.add(idx)
            break


def get(heap: List[Tuple[int, int]]) -> int:
    while heap:
        data, idx = heappop(heap)
        if idx not in removed:
            return data
    return 0


def solution(operations: List[str]) -> List[int]:
    for idx, op in enumerate(operations):
        cmd, data = op.split()

        if cmd == "I":
            insert(int(data), idx)
        elif data == "1":
            delete(maxheap)
        else:
            delete(minheap)

    return [-get(maxheap), get(minheap)]
