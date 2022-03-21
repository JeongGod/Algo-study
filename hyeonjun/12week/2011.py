import sys
input = sys.stdin.readline

if __name__ == "__main__":
    password = str(input().rstrip())

    if not password:
        print(0)
        exit()

    dp = [[0, 0] for _ in range(len(password))]
    if int(password[0]):
        dp[0][0] = 1
    for i in range(len(password)-1):
        if int(password[i+1]):
            dp[i+1][0] = dp[i][0] + dp[i][1]
        if int(password[i:i+2]) < 27:
            dp[i+1][1] = dp[i][0]
    print(sum(dp[-1]) % 1000000)
