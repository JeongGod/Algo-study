def solution(tickets):
    tickets = sorted(tickets, key=lambda x: (x[0], x[1]))
    records = dict()

    for start, arrive in tickets:
        if start in records:
            records[start].append(arrive)
        else:
            records[start] = [arrive]

    path = []

    stack = ["ICN"]
    while stack:
        top = stack[-1]
        if top not in records or len(records[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(records[top].pop(0))

    print(path[::-1])

    return path[::-1]
