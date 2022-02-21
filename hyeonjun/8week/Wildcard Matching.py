class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(p)+1)]
        dp[0][0] = 1

        for i in range(len(p)):
            if p[i] == '*':
                dp[i+1][0] = dp[i][0]

        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == s[j] or p[i] == '?':
                    dp[i+1][j+1] |= dp[i][j]
                if p[i] == '*':
                    dp[i+1][j+1] |= dp[i+1][j] or dp[i][j+1]

        return dp[-1][-1]
