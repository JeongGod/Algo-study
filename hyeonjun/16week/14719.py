import sys
input = sys.stdin.readline


def fill():
    res = 0
    for i in range(1, W-1):
        tmp = min(max(blocks[:i]), max(blocks[i+1:]))
        if blocks[i] < tmp:
            res += tmp - blocks[i]
    return res


if __name__ == "__main__":
    H, W = map(int, input().split())
    blocks = list(map(int, input().split()))
    print(fill())
