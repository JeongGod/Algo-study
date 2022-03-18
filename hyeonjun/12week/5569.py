import sys
input = sys.stdin.readline

if __name__ == '__main__':
    w, h = map(int, input().split())
    dp = [[[0 for _ in range(4)] for _ in range(w)]for _ in range(h)]

    for i in range(w-1):
        dp[0][i+1][1] = 1
    for i in range(h-1):
        dp[i+1][0][0] = 1

    for i in range(h-1):
        for j in range(w-1):
            dp[i+1][j+1] = [dp[i][j+1][2]+dp[i][j+1][0], dp[i+1]
                            [j][3] + dp[i+1][j][1],  dp[i][j+1][1], dp[i+1][j][0]]
    print(sum(dp[-1][-1]) % 100000)
