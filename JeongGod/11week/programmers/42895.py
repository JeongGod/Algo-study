def calc(a, b):
    result = set()
    for i in a:
        for j in b:
            result.add(i+j)
            result.add(i-j)
            result.add(j-i)
            result.add(i*j)
            if j != 0:
                result.add(i // j)
            if i != 0:
                result.add(j // i)
    return result

def solution(N : int, number : int):
    dp = [set() for _ in range(10)]

    for i in range(1, 9):
        # dp[i] = dp[i-1] 사칙연산 dp[1], dp[i-2] dp[2] dp[i-3] dp[3] ... dp[1] dp[i-1]
        # dp[3] = dp[2] + dp[1] , dp[1] + dp[2]
        dp[i].add(int(str(N)*i))
        for j in range(1, i//2 + 1):
            dp[i] |= calc(dp[i-j], dp[j])
        if number in dp[i]:
            return i
    return -1
