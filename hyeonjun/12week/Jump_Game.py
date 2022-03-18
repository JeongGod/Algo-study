class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        target = length - 1
        for index in range(length - 2, -1, -1):
            step = nums[index]
            if index + step >= target:
                target = index

        return True if not target else False
