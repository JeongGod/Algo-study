from collections import deque
def solution(number, k):
    answer = ''
    q = deque()
    for i in range(len(number)):
        if not q :
            q.append(number[i])
            continue
        if(k and q and q[-1] >= number[i]):
            q.append(number[i])
            continue
        else:
            while (k and q and q[-1] < number[i]):
                q.pop()
                k -=1 
            q.append(number[i])
    for i in range(len(q) - k):
        answer += q[i]
    return answer