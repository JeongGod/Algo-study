# 수식의 최대길이 19 -> 숫자 10개 + 연산자 9개
# 9c1 + 9c2 + ... 9c5
# 위 경우에서도 안되는 케이스가 계속 걸러짐 -> 딱 붙어있는 연산자를 선택할 때
# 9c6 부터는 무조건 위와같은 경우가 생기므로 고려 x
from collections import deque
import sys

def combination(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i, el in enumerate(arr):
        rest_arr = arr[i+2:]
        for c in combination(rest_arr, n-1):
            result.append([el]+c)

    return result

def calc(arr, case):
    visited = [False for _ in range(len(arr))]
    q = deque()
    for i in range(len(arr)):
        if(visited[i]):
            continue
        if(i not in case):
            q.append(arr[i])
        else:
            string = ""
            string += q.pop() + arr[i] + arr[i+1]
            q.append(str(eval(string)))
            visited[i+1] = True
        
    while len(q) > 1:
        string = ""
        string += q.popleft() + q.popleft() + q.popleft()
        q.appendleft(str(eval(string)))
        
    return int(q.popleft())
        
        
n = int(input())
formula = input()

# 연산자 위치 인덱스 모음
operator = []
for i in range(1, n, 2):
    operator.append(i)
answer = -(sys.maxsize+1)
if(n == 1):
    answer = max(answer, int(formula))
# 괄호를 끼울 연산자 선택
for i in range(1, (len(operator) + 1)//2 + 1):
    for case in combination(operator, i): # 선택된 괄호 연산자
        answer = max(answer, calc(formula, case))

print(answer)
        