import sys
input = sys.stdin.readline


def count(num):
    res = 0
    for i in num:
        if int(i) % 2:
            res += 1
    return res


def divide(n, res):
    global min_ans, max_ans
    if len(n) == 1:
        min_ans = min(min_ans, res)
        max_ans = max(max_ans, res)
    elif len(n) == 2:
        tmp = str(int(n[0]) + int(n[1]))
        divide(tmp, res + count(tmp))
    else:
        for i in range(len(n) - 2):
            for j in range(i+1, len(n)-1):
                tmp = str(int(n[:i+1]) + int(n[i+1:j+1]) + int(n[j+1:]))
                divide(tmp, res + count(tmp))


if __name__ == "__main__":
    N = str(input().rstrip())
    min_ans, max_ans = float('inf'), 0
    divide(N, count(N))
    print(min_ans, max_ans)
