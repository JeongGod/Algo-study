import sys
sys.setrecursionlimit(10**6)

def topdown(n, l, r):
    global dp
    if arr[n] == 0 :
        return 0
 
    if dp[n][l][r] != None:
        return dp[n][l][r]
 
    dp[n][l][r] = min(topdown(n+1, arr[n],r) + move[l][arr[n]], topdown(n+1, l, arr[n]) + move[r][arr[n]])
    return dp[n][l][r]
    
move = [[1, 2, 2, 2, 2],
       [3, 1, 3, 4, 3],
       [4, 3, 1, 3, 4],
       [3, 4, 3, 1, 3],
       [4, 3, 4, 3, 1],
       ]

arr = list(map(int, sys.stdin.readline().split()))
dp = [[[None for _ in range(5)] for _ in range(5)] for _ in range(len(arr))]

answer = topdown(0, 0, 0)

print(answer)