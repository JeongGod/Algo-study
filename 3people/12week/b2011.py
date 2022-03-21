cipher = list(map(int, list(input())))
dp = [0] * (len(cipher) + 1)
dp[0] = dp[1] = 1

cipher = [0] + cipher

if cipher[1] == 0:
  print(0)
  exit(0)

for i in range(2, len(cipher)):
  first = cipher[i]
  tenth = cipher[i-1] * 10 + cipher[i]
  if first > 0:
    dp[i] += dp[i-1]
  if tenth >= 10 and tenth <= 26:
    dp[i] += dp[i-2]
print(dp[len(cipher) - 1] % 1000000)