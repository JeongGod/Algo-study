import sys

input = sys.stdin.readline

def main():
    N, M, k = map(int, input().split())
    dp = [[0] * (M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][0] = 1
    for j in range(1, M+1):
        dp[0][j] = 1

    # dp[a의 개수][z의 개수] = 가능한 갯수
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    if dp[N][M] < k:
        return -1

    def a_z(n, m, limit):
        # a가 올 수 있는 경우
        if dp[n-1][m] >= limit:
            return "a", limit
        # z가 와야하는 경우
        return "z", limit - dp[n-1][m]

    result = ""
    while True:
        if N == 0 or M == 0:
            break
        val, k = a_z(N, M, k)
        result += val
        # a를 하나 썼으니 a의 개수를 하나 줄인다.
        if val == "a":
            N -= 1
        # z를 하나 썼으니 z의 개수를 하나 줄인다.
        else:
            M -= 1
    # 남아있는 a의 개수나 z의 개수를 붙인다.
    while N != 0:
        result += "a"
        N -= 1
    while M != 0:
        result += "z"
        M -= 1
    return result
    

if __name__ == "__main__":
    print(main())

