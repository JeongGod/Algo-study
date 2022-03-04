import sys
input = sys.stdin.readline

n = int(input())
arr = []
dp = []
for _ in range(n):
  arr.append(int(input()))

if n == 1:
  print(arr[0])
  exit(0)
elif n == 2:
  print(max(arr[0] + arr[1], arr[1]))
  exit(0)
else:
  dp.append(arr[0])
  dp.append(max(arr[0] + arr[1], arr[1]))
  dp.append(max(arr[0] + arr[2], arr[1] + arr[2]))

  for i in range(3, n):
    dp.append(max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i]))
  print(dp[-1])