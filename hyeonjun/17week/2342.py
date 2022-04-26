import sys
input = sys.stdin.readline


def calc_cost(target, order):
    if not target:
        return 2
    if target == order:
        return 1
    if (target+order) % 2:
        return 3
    return 4


if __name__ == "__main__":
    orders = list(map(int, input().split()))
    orders.pop()
    length = len(orders)
    dp = [[[sys.maxsize for _ in range(5)] for _ in range(5)]
          for _ in range(length+1)]
    dp[-1][0][0] = 0
    for i in range(length):
        for j in range(5):
            for k in range(5):
                cost = calc_cost(k, orders[i])
                dp[i][orders[i]][j] = min(
                    dp[i][orders[i]][j], dp[i-1][k][j]+cost)
        for j in range(5):
            for k in range(5):
                cost = calc_cost(k, orders[i])
                dp[i][j][orders[i]] = min(
                    dp[i][j][orders[i]], dp[i-1][j][k] + cost)
    ans = sys.maxsize
    for i in range(5):
        for j in range(5):
            ans = min(ans, dp[length-1][i][j])
    print(ans)
