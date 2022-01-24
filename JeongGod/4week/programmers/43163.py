from collections import deque


def check(start, target):
    cnt = 0
    for x, y in zip(start, target):
        if x != y:
            cnt += 1
        if cnt > 1:
            return False
    return True

def solution(begin, target, words):
    # 타겟에 없는 경우
    if not target in words:
        return 0
    answer = 0
    dq = deque([(begin, 0)])
    visited = [False] * len(words)
    # BFS
    while dq:
        cur, cost = dq.popleft()
        if cur == target:
            return cost
        for i in range(len(words)):
            if visited[i] or not check(cur, words[i]):
                continue
            
            visited[i] = True
            dq.append((words[i], cost+1))
    return answer
