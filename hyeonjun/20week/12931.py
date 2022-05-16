import sys
input = sys.stdin.readline

if __name__ == '__main__':
    ans = 0
    N = int(input())
    arrB = list(map(int, input().split()))

    while True:
        flag, flag2 = True, True
        for i in range(N):
            if arrB[i]:
                flag = False

            if arrB[i] % 2:
                ans += 1
                flag2 = False
                arrB[i] -= 1

        if flag:
            break

        if flag2:
            for i in range(N):
                arrB[i] /= 2
            ans += 1

    print(ans)
