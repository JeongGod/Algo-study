
def solution(s):
    stack = []
    for letter in s:
        if not stack or stack[-1] != letter:
            stack.append(letter)
        else:
            stack.pop()

    return 0 if stack else 1
