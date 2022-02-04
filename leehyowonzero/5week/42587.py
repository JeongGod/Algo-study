from collections import deque

def getmax(q):
    q = sorted(q, reverse = True, key = lambda x : str(x)[-1])
    if(len(q) == 1):
        return q[0]%10
    return q[0]%10

def solution(priorities, location):
    answer = 0 
    priorities[location] += 10
    q = deque(priorities)
    while q:
        now = q.popleft()
        if not(q):
            answer += 1
            break
        if(now%10 >= getmax(q)):
            answer += 1
            if(now > 10):
                break
        else:
            q.append(now)
    return answer