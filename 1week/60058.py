import sys
sys.setrecursionlimit(10**7)

def check(string):  
    q = []
    for el in string:
        if el == '(':
            q.append(el)
        else:
            if(q):
                q.pop()
    if(q):
        return False
    else:
        return True

def seperate(string):
    x = 0
    y = 0
    for i in range(len(string)):
        if(string[i] == '('):
            x += 1
        else:
            y += 1
        if(x == y and x != 0):
            return string[:i+1], string[i+1:]
    return 
def reverse(string):
    s = ''
    for el in string:
        if(el == '('):
            s += ')'
        else:
            s += '('
    return s

def solution(p):
    answer = ''
    # 1
    if(p == ''):
        return ''
    # 2
    u , v = seperate(p)
    if(check(u) == True):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = u[1: -1]
        reversedu = reverse(u)
        answer += reversedu
    return answer