from typing import List


def check(node: int) -> None:
    checked[node] = True

    for adj, isconnected in enumerate(connected[node]):
        if not checked[adj] and isconnected == 1:
            check(adj)


def solution(n: int, computers: List[List[int]]):
    global checked, connected
    checked = [False for _ in range(n)]
    connected = computers

    answer: int = 0
    for node in range(n):
        if not checked[node]:
            check(node)
            answer += 1
    return answer


# 2
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# 1
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
