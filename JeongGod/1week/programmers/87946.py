answer = -1


def solution(k, dungeons):
    visited = [0] * len(dungeons)

    def dfs(tired, cnt):
        global answer
        for idx in range(len(dungeons)):
            if not visited[idx] and tired >= dungeons[idx][0]:
                visited[idx] = 1
                tired -= dungeons[idx][1]
                dfs(tired, cnt + 1)
                tired += dungeons[idx][1]
                visited[idx] = 0
        answer = max(answer, cnt)

    dfs(k, 0)
    return answer
