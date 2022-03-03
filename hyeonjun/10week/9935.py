import sys
input = sys.stdin.readline


def explode(string):
    stack = []
    for word in string:
        stack.append(word)
        if stack[-1] == target[-1] and stack[-target_length:] == target:
            for _ in range(target_length):
                stack.pop()

    if stack:
        return "".join(stack)
    else:
        return 'FRULA'


if __name__ == "__main__":
    string = list(input().rstrip())
    target = list(input().rstrip())
    target_length = len(target)
    print(explode(string))
