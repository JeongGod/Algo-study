from collections import deque

def removepair(s):
    q = deque()
    q.append(s[0])
    for i in range(1, len(s)):
        if (q and q[-1] == s[i]):
            q.pop()
        else:
            q.append(s[i])
    return "".join(q)

def solution(s):
    while s:
        nexts = removepair(s)
        if(nexts == s):
            return 0
        s = nexts
    return 1
