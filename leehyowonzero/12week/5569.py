# dp = [[[x, y, z, u] for _ in range(w)] for _ in range(h)], => [아래로 1스택, 오른쪽으로 1스택, 아래로 2스택, 오른쪽으로 2스택]
w, h = map(int, input().split())
dp = [[[0, 0, 0, 0] for _ in range(w)] for _ in range(h)]


for i in range(1, w):
    dp[0][i] = [0,0,0,1]
for i in range(1, h):
    dp[i][0] = [0,0,1,0]

for i in range(1, h):
    for j in range(1, w):
        dp[i][j] = [dp[i-1][j][3], dp[i][j-1][2], dp[i-1][j][0] + dp[i-1][j][2], dp[i][j-1][1] + dp[i][j-1][3]]

print(sum(dp[h-1][w-1])%100000)