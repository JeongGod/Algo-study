def dfs(c, i):
    if not c[i][i]:
        return False
    c[i][i] = 0
    for j in range(len(c)):
        if c[i][j]:
            dfs(c, j)
    return True


def solution(n, computers):
    answer = 0
    for i in range(n):
        if computers[i][i] and dfs(computers, i):
            answer += 1
    return answer
