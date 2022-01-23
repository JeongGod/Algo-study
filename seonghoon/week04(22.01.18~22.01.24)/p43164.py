from collections import defaultdict, deque
from typing import DefaultDict, Deque, List, Set, Tuple


TicketDict = DefaultDict[str, List[Tuple[int, str]]]


def get_next_airports(tickets: List[List[str]]) -> TicketDict:
    next_airports: TicketDict = defaultdict(list)

    for idx, (start, dest) in enumerate(sorted(tickets, key=lambda x: x[1])):
        next_airports[start].append((idx, dest))

    return next_airports


def solution(tickets: List[List[str]]) -> List[str]:
    numoftickets: int = len(tickets)
    next_airports: TicketDict = get_next_airports(tickets)

    que: Deque[Tuple[List[str], Set[int]]] = deque()

    que.append((["ICN"], set()))

    while que:
        paths, used = que.popleft()

        for tid, next_ in next_airports[paths[-1]]:
            if tid in used:
                continue

            next_paths: List[str] = paths + [next_]

            if len(next_paths) == numoftickets + 1:
                return next_paths

            que.append((next_paths, used | set([tid])))

    return []


# ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(
    solution(
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    )
)
