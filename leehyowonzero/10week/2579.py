n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [[0, 0] for _ in range(n)] # [ , ] 1칸전진으로 왔는가, 2칸전진으로 왔는가  
dp[0][0] = arr[0]

for i in range(1, n):
    if(i == 1):
        dp[i][0] = dp[i-1][0] + arr[i]
        dp[i][1] = arr[i]
        continue
    dp[i][0] = dp[i-1][1] + arr[i]
    dp[i][1] = max(dp[i-2]) + arr[i]
print(max(dp[n-1]))