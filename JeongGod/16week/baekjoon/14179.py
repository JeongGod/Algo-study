import sys

input = sys.stdin.readline


def make_maxlist(start, end, g):
    li = []
    max_val = 0
    for i in range(start, end, g):
        max_val = max(max_val, blocks[i])
        li.append(max_val)
    return li

if __name__ == "__main__":
    H, W = map(int, input().split())
    blocks = list(map(int, input().split()))
    
    max_blocks = make_maxlist(0, W, 1)
    min_blocks = make_maxlist(W-1, -1, -1)[::-1]

    answer = 0
    for idx, (a, b) in enumerate(zip(max_blocks, min_blocks)):
        answer += min(a, b) - blocks[idx]
    print(answer)
