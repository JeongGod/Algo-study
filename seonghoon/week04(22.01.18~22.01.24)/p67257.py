from itertools import permutations
from typing import List


def calculate(expression: str, ops: List[str]) -> int:
    if expression.isdigit():
        return int(expression)

    curop, nextops = ops[0], ops[1:]
    splitted: List[int] = [calculate(exp, nextops) for exp in expression.split(curop)]
    return eval(f"{curop}".join(map(str, splitted)))


def solution(expression: str):
    answer: int = 0
    for perm in permutations(["+", "-", "*"]):
        answer = max(answer, abs(calculate(expression, list(perm))))
    return answer


# 60420
print(solution("100-200*300-500+20"))
# 300
print(solution("50*6-3*2"))
