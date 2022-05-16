class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [[0, 0] for _ in range(len(nums)+1)]

        for idx, money in enumerate(nums):
            dp[idx+1][0] = max(dp[idx][0], dp[idx][1])
            dp[idx+1][1] = dp[idx][0] + money

        return max(dp[-1])
