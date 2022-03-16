import sys

input = sys.stdin.readline

def make_dp(pizza : list[int]) -> list[list[int]]:
    length = len(pizza)
    dp = [[0] * length for _ in range(length)]

    for i in range(length):
        dp[i][i] = pizza[i]
    
    for jump in range(1, length):
        for start in range(length):
            end = (start + jump) % length
            if start -1 == end:
                continue
            dp[start][end] = dp[start][end-1] + dp[end][end]
    
    return dp

def binary_search_left(new_target : int, new_b : list[int]) -> int:
    left, right = 0, len(new_b) - 1
    while left <= right:
        mid = (left + right) // 2
        if new_target > new_b[mid]:
            left = mid+1
        else:
            right = mid-1
    return left

def binary_search_right(new_target : int, new_b : list[int]) -> int:
    left, right = 0, len(new_b) - 1
    while left <= right:
        mid = (left + right) // 2
        if new_target >= new_b[mid]:
            left = mid+1
        else:
            right = mid-1
    return left

def solution(target : int, m : int, n : int, pizza_a : list[int], pizza_b : list[int]) -> int:
    """
    1. 원형이다.
    2. "연속된 조각들"이다.

    1. 먼저 각각의 dp테이블을 구한다.
    2. 각 dp테이블의 값들을 일차원 리스트로 펼친 뒤 정렬한다.
    3. 각 리스트를 투포인터를 이용하여 두 개의 피자를 합쳤을 때 값이 나오는지 확인한다.
    """
    answer = 0

    dp_a = make_dp(pizza_a)
    dp_b = make_dp(pizza_b)

    new_a = [v for arr in dp_a for v in arr if v != 0]
    # A피자에 완성된 누적합이 있을 경우
    answer += new_a.count(target)
    # B피자에 완성된 누적합이 있을 경우
    new_a.append(0)
    new_b = sorted([v for arr in dp_b for v in arr if v != 0])

    for val in new_a:
        new_target = target - val
        if new_target <= 0:
            continue
        # target중 가장 왼쪽에 있는 친구를 찾는다.
        l_idx = binary_search_left(new_target, new_b)
        # target중 가장 오른쪽에 있는 친구를 찾는다.
        r_idx = binary_search_right(new_target, new_b)

        if not (0 <= l_idx < len(new_b)):
            continue
        if new_b[l_idx] == new_target:
            answer += (r_idx - l_idx)

    return answer


if __name__ == "__main__":
    T = int(input())
    M, N = map(int, input().split())
    pizza_a = [int(input()) for _ in range(M)]
    pizza_b = [int(input()) for _ in range(N)]
    print(solution(T, M, N, pizza_a, pizza_b))
