from collections import deque

def check(s):
    q = deque()
    for el in list(s):
        if(len(q) > 0 and (ord(el)-ord(q[-1]) == 1 or ord(el)-ord(q[-1]) == 2)):
            q.pop()
        else:
            q.append(el)
    if(len(q)):
        return 0
    return 1

def solution(s): # 만약 이번 문자열로 올바른 괄호 문자열을 만들 수 있다면, 한칸씩 rotate 작업을 실시한 문자열은 올바른 괄호일 수 없으므로 건너뛸 수 있다.
    answer = 0
    i = 0
    while i < len(s): 
        if(check(s)):
            answer += 1
            s = s[2:] + s[0:2]
            i += 2
        else:
            s = s[1:] + s[0]
            i += 1
    return answer