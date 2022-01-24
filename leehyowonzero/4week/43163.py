from collections import deque

def transpossible(a, b):
    cnt = 0 
    if(len(a) != len(b)):
        return False
    for i in range(len(a)):
        if(a[i] != b[i]):
            cnt += 1
    if(cnt == 1):
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0 # 변환횟수
    visited = [False for _ in range(len(words))]
    q = deque()
    q.append(begin)
    while(q):
        turnlen = len(q)
        for _ in range(turnlen): # 동일한 변환 횟수를 거친 문자열들
            a = q.popleft()
            if(a == target):
                return answer
            for i in range(len(words)):
                if(visited[i] != False):
                    continue
                if(transpossible(a, words[i])):
                    q.append(words[i])
                    visited[i] = True 
        answer += 1
    return 0