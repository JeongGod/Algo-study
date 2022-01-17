from typing import List


OPENS = set(["(", "[", "{"])
CLOSES = {"(": ")", "[": "]", "{": "}"}


def iscorrect(string: str) -> bool:
    stack: List[str] = []

    for char in string:
        if stack and stack[-1] in OPENS and CLOSES[stack[-1]] == char:
            stack.pop()
        else:
            stack.append(char)

    return not stack


def solution(s: str) -> int:
    return sum(int(iscorrect(s[idx:] + s[:idx])) for idx in range(len(s)))


# 3
print(solution("[](){}"))
# 2
print(solution("}]()[{"))
# 0
print(solution("[)(]"))
# 0
print(solution("}}}"))
