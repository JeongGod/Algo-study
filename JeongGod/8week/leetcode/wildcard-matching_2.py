class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        
        # 빈 칸, 빈 칸일 경우
        dp[0][0] = True
        for i in range(1, len(p)+1):
            dp[0][i] = dp[0][i-1] and p[i-1] == "*"
        
        for j in range(1, len(s)+1):
            for i in range(1, len(p)+1):
                if s[j-1] == p[i-1] or p[i-1] == "?":
                    dp[j][i] = dp[j-1][i-1]
                elif p[i-1] == "*":
                    dp[j][i] = dp[j-1][i] or dp[j][i-1]

        return dp[len(s)][len(p)]
