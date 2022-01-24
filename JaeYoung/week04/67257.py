from itertools import permutations
from typing import List, Set
import re


def solution(expression):
    answer: List[int] = []

    ope: List[str] = re.split("[0-9]+", expression)[1:-1]
    op_combinations: List[Set] = list(permutations(set(ope)))

    for op_combi in op_combinations:
        operators: List[str] = ope[:]
        numbers: List[str] = re.split("[*+-]", expression)
        print(numbers)

        for op in op_combi:
            while op in operators:
                idx = operators.index(op)
                numbers[idx] = str(eval(numbers[idx] + op + numbers[idx+1]))
                del numbers[idx+1]
                del operators[idx]

        answer.append(abs(int(numbers[0])))

    return max(answer)
