import sys
input = sys.stdin.readline


def connect_bridge():
    for idx1, info in enumerate(connect_info):
        for idx2, city in enumerate(info):
            if city:
                dp[idx1][idx2] = 1


def floyd_warshall():
    for k in range(N):
        dp[k][k] = 1
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


def can_go():
    start = schedule[0]
    for city in schedule[1:]:
        if dp[start-1][city-1] != float('inf'):
            start = city
        else:
            return 'NO'
    return 'YES'


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    connect_info = [list(map(int, input().split())) for _ in range(N)]
    schedule = list(map(int, input().split()))
    dp = [[float('inf') for _ in range(N)] for _ in range(N)]
    connect_bridge()
    floyd_warshall()
    print(can_go())
