class Solution:
    def canJump(self, nums: List[int]) -> bool:
        MaxCanjump = 0
        for i in range(len(nums)):
            if(i <= MaxCanjump):
                MaxCanjump = max(MaxCanjump,i + nums[i])
            else:
                return False
            
            if(MaxCanjump >= len(nums) - 1):
                return True