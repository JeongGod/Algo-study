import sys
INF = sys.maxsize

def floyd(dp, n):
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp
    


def solution(n, s, a, b, fares):
    answer = INF
    
    dp = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][i] = 0
    for fare in fares:
        c, d, f = fare
        dp[c][d] = f
        dp[d][c] = f
    
    dp = floyd(dp, n)
    
    for k in range(1, n+1):
        answer = min(answer, dp[s][k] + dp[k][a] + dp[k][b])
        
    return answer