from collections import defaultdict


def dfs(visited : set, trip : list, target : int):
    if len(visited) == target:
        return trip
    cur = trip[-1]
    for idx, air in airport[cur]:
        if idx in visited:
            continue
        visited.add(idx)
        result = dfs(visited, trip + [air], target)
        visited.discard(idx)
        # 알파벳 순서로 정렬해놨으니 답을 찾는 경우가 바로 끝
        if result:
            return result


def solution(tickets):
    global answer, airport
    answer = []
    airport = defaultdict(list)

    for idx, [start, end] in enumerate(tickets):
        airport[start].append((idx, end))
    # 알파벳 순서로 정렬
    for k in airport:
        airport[k].sort(key=lambda x:x[1])
    visited = set()
    return dfs(visited=visited, trip=["ICN"], target=len(tickets))
