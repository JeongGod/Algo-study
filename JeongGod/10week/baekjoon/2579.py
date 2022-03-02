import sys

input = sys.stdin.readline

def solution(num : int, stairs : list[int]) -> int:
    if num == 1:
        return stairs[0]
    elif num == 2:
        return stairs[0] + stairs[1]
    dp = [0] * num
    """
    dp[i][0] = 하나도 밟지 않고 새로운 친구
    dp[i][1] = 하나를 밟은 친구
    """
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    for i in range(3, num):
        dp[i] = max(stairs[i] + dp[i-2], stairs[i] + stairs[i-1] + dp[i-3])
    return dp[num-1]

if __name__ == "__main__":
    N = int(input())
    stairs = list(int(input()) for _ in range(N))
    print(solution(N, stairs))
