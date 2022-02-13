import sys
input = sys.stdin.readline


def calc():
    ans = 0
    width = 0
    height = 0
    for i in range(1, 367):
        calendar[i] += calendar[i-1]
        if not calendar[i]:
            ans += width*height
            width = 0
            height = 0
        else:
            width += 1
            height = max(height, calendar[i])
    return ans


if __name__ == "__main__":
    N = int(input())
    calendar = [0 for _ in range(367)]
    for _ in range(N):
        s, e = map(int, input().split())
        calendar[s] += 1
        calendar[e+1] -= 1
    print(calc())
