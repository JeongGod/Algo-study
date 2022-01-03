from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    while(q):
        now = q.popleft()
        cnt = 0
        for el in q:
            cnt += 1
            if(now > el):
                break
        answer.append(cnt)   
    return answer