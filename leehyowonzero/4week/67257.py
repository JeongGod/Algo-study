import re
import copy
from itertools import permutations
from collections import deque
def solution(expression):
    answer = 0
    permutationcase = list(permutations(['-','+','*']))
    SplitedExpression = re.split(r'(\D)',expression) # 정규식을 이용하여 연산자 기준으로 스플릿
    
    for case in permutationcase: # 모든 연산자 우선순위 경우의수
        leastExpression = deque(SplitedExpression)
        for operator in case: # 우선순위가 높은 연산자와 만나면 계산
            q = deque()
            while leastExpression:
                if(leastExpression[0] == operator):
                    q.append(str(eval(q.pop() + leastExpression.popleft() + leastExpression.popleft())))
                else:
                    q.append(leastExpression.popleft())
            leastExpression = q.copy()
        answer = max(answer, abs(int(q[0])))
    return answer