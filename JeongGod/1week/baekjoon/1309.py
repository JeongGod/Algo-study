import sys

input = sys.stdin.readline

N = int(input())

dp = list([0] * 3 for _ in range(N))
for i in range(3):
    dp[0][i] = 1

"""
dp[i][0] => i층에 아무것도 놓지 않는 경우
dp[i][1] => i층에 1번째 칸에 놓는 경우
Dp[i][2] => i층에 2번째 칸에 놓는 경우
"""
for i in range(1, N):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901
print(sum(dp[N-1]) % 9901)
