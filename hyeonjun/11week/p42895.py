def solution(N, number):
    answer = -1
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i-j]:
                    dp[i].add(k+l)
                    dp[i].add(k*l)
                    dp[i].add(k-l)
                    if l:
                        dp[i].add(k//l)

        if number in dp[i]:
            answer = i
            break

    return answer
