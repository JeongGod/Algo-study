def check(target):
    stack = []
    for elm in target:
        if not stack:
            stack.append(elm)
        else:
            if (
                (elm == "]" and stack[-1] == "[")
                or (elm == "}" and stack[-1] == "{")
                or (elm == ")" and stack[-1] == "(")
            ):
                stack.pop()
            else:
                stack.append(elm)
    return False if stack else True


def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s[i:] + s[:i]):
            answer += 1
    return answer
