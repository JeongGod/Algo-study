import sys
from collections import deque


def bfs(K):
    que = deque()
    que.append(1)
    path[1] = 0

    while que:
        start = que.popleft()

        for arrive in range(1, len(graph)):

            if graph[start][arrive] == 0:
                continue

            if (path[arrive] > path[start] + graph[start][arrive]
                    and path[start] + graph[start][arrive] <= K):

                path[arrive] = path[start] + graph[start][arrive]
                que.append(arrive)


def solution(N, road, K):
    answer = 0
    global path, graph

    path = [sys.maxsize for _ in range(N+1)]  # 1번마을부터 N 번 마을 까지의 거리
    graph = [[0] * (N+1) for _ in range(N+1)]  # 마을끼리 가는 거리 입력

    for info in road:
        start, arrive, w = info

        if graph[start][arrive] == 0 and graph[arrive][start] == 0:
            graph[start][arrive] = w
            graph[arrive][start] = w
        else:
            # 중복되는 값이 있는 경우는 더 작은 w를 사용
            if w < graph[start][arrive]:
                graph[start][arrive] = w
                graph[arrive][start] = w

    bfs(K)
    answer = len([i for i in path if i <= K])

    return answer
