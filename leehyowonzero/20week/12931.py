n = int(input())
arr = list(map(int,input().split()))
dp = [[0, 0] for _ in range(1001)]

for i in range(1, 1001):
    if(i % 2 == 0):
        dp[i][0] = dp[i//2][0] + 1
        dp[i][1] = dp[i//2][1]
    else:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][1] + 1

maxhalf = 0
sumplus = 0
for el in arr:
    maxhalf = max(maxhalf, dp[el][0])
    sumplus += dp[el][1]
print(maxhalf + sumplus)