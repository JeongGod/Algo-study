import re
from collections import deque
from itertools import permutations
from typing import List


def calc(num_dq : List, oper_dq : List, oper : str) -> List:
    for _ in range(len(oper_dq)):
        # 왼쪽부터 계산한다.
        a = num_dq.popleft()
        # 계산할 기호를 뽑는다.
        op = oper_dq.popleft()
        # 계산할 기호가 현재 우선순위와 맞는지 체크한다.
        if op != oper:
            num_dq.append(a)
            oper_dq.append(op)
            continue
        # 계산한다.
        if op == "+":
            num_dq[0] = a+num_dq[0]
        elif op == "*":
            num_dq[0] = a*num_dq[0]
        else:
            num_dq[0] = a-num_dq[0]
    num_dq.append(num_dq.popleft())

    return num_dq, oper_dq

def solution(expression):
    """
    1. 연산자의 우선순위를 마음대로 정할 수 있다.
    2. 계산된 절댓값이 가장 큰 값을 찾아라.

    3! => 6가지
    """
    answer = 0
    operand = ["+", "-", "*"]
    number = re.compile("[0-9]*")
    origin_num_dq = []
    for i in number.findall(expression):
        if i == "":
            continue
        origin_num_dq.append(int(i))
    oper = re.compile("[*+-]")
    origin_oper_dq = oper.findall(expression)

    for opers in permutations(operand, 3):
        num_dq = deque(origin_num_dq[:])
        oper_dq = deque(origin_oper_dq[:])
        for oper in opers:
            # oper에 해당하는 친구만 계산
            num_dq, oper_dq = calc(num_dq, oper_dq, oper)
        if abs(num_dq[0]) > answer:
            answer = abs(num_dq[0])
    return answer
