class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        """
        1. two pointer
        """
        if len(nums) < 3:
            return []
        
        for start in range(len(nums)):
            left = start + 1
            right = len(nums) - 1
            while left < right:
                result = nums[start] + nums[left] + nums[right]
                if result == 0:
                    answer.add((nums[start], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif result < 0:
                    left += 1
                else:
                    right -= 1
        return answer
