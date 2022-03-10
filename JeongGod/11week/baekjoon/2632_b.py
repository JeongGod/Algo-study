import sys

input = sys.stdin.readline

def make_arr(length : int, pizza : list[int]) -> list[int]:
    dp = [0] * 2_000_001
    for start in range(length):
        result = 0
        for jump in range(length - 1):
            result += pizza[(start + jump) % length]
            if T < result:
                break
            dp[result] += 1
    return dp

def solution(pizza_a : list[int], pizza_b : list[int]) -> int:
    # 1. 누적합을 구한다.
    dp_a = make_arr(N, pizza_a)
    dp_a[sum(pizza_a)] += 1
    dp_a[0] = 1
    dp_b = make_arr(M, pizza_b)
    dp_b[sum(pizza_b)] += 1
    dp_b[0] = 1
    
    # 2. 가능한 경우의 수를 찾는다.
    answer = 0
    for s in range(T+1):
        answer += dp_a[s] * dp_b[T-s]
    return answer


if __name__ == "__main__":
    T = int(input())
    N, M = map(int, input().split())
    pizza_a = [int(input()) for _ in range(N)]
    pizza_b = [int(input()) for _ in range(M)]
    print(solution(pizza_a, pizza_b))
