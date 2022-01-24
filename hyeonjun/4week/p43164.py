from collections import deque


def dfs(airport, route, route_cnt):
    cnt = 0
    while cnt < len(bridge[airport]):
        next_airport = bridge[airport].popleft()
        route.append(next_airport)
        route_cnt -= 1

        if not route_cnt:
            return route

        tmp = dfs(next_airport, route, route_cnt)
        if tmp:
            return tmp

        bridge[airport].append(next_airport)
        route.pop()
        route_cnt += 1
        cnt += 1

    return 0


def solution(tickets):
    global bridge

    tickets.sort()
    airports = set()
    for ticket in tickets:
        airports.add(ticket[0])
        airports.add(ticket[1])

    bridge = {airport: deque() for airport in airports}
    for ticket in tickets:
        bridge[ticket[0]].append(ticket[1])

    route_cnt = len(tickets)
    return dfs('ICN', ['ICN'], route_cnt)
