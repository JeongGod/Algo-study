import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    if M:
        broken_buttons = set(input().split())
    else:
        broken_buttons = []

    ans = abs(100-N)
    for i in range(1000001):
        for j in str(i):
            if j in broken_buttons:
                break
        else:
            ans = min(ans, len(str(i))+abs(i-N))

    print(ans)
