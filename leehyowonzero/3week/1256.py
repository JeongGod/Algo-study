n , m, k = map(int,input().split())

dp = [[0 for _ in range(m+2)] for _ in range(n+2)]
for i in range(0,n+1):
	for j in range(0,m+1):
		if( i == 0 or j == 0):
			dp[i][j] = 1

# dp[n][m] : "a" n개 "z" m개로 만들 수 있는 문자열 조합 수
for i in range(1,n+1):
	for j in range(1,m+1):
		if(i == 1 and j != 0):
			dp[i][j] = j + 1
		elif(j == 1 and i != 0):
			dp[i][j] = i + 1
		else:
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
		# print(dp[i][j])
ans = ""
if(dp[n][m] < k):
	print("-1")
	exit()
while (n > 0 or m > 0 ) :
	if(dp[n-1][m] >= k):
		# print("a붙여야해")
		ans += "a"
		n -= 1		
	else:
		k -= dp[n-1][m]
		# print("z 붙여야해")		
		ans += "z"
		m -= 1
print(ans)