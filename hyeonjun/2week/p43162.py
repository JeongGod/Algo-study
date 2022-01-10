def dfs(now, computers):
    network[now] = 1
    for i, num in enumerate(computers[now]):
        if not network[i] and num:
            dfs(i, computers)
    return 0


def solution(n, computers):
    global network
    answer = 0
    network = [0 for _ in range(n)]
    for i, computer in enumerate(computers):
        if not network[i]:
            dfs(i, computers)
            answer += 1

    return answer
