from typing import List


def isRightString(string: str) -> bool:
    stack: List[str] = []

    for x in string:
        if x == "(" or x == "[" or x == "{":
            stack.append(x)
        elif x == ")":
            if len(stack) and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif x == "]":
            if len(stack) and stack[-1] == "[":
                stack.pop()
            else:
                return False
        elif x == "}":
            if len(stack) and stack[-1] == "{":
                stack.pop()
            else:
                return False

    return False if len(stack) else True


def solution(s) -> int:
    answer = 0
    answer += 1 if isRightString(s) else 0  # 초기 문자열 올바른 괄호인지 판단

    for i in range(1, len(s)):
        new_string: str = s[i:] + s[:i]  # 문자열 회전
        answer += 1 if isRightString(new_string) else 0  # 회전 문자열 올바른 괄호인지 판단

    return answer