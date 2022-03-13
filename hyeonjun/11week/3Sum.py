class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()

        for i in range(len(nums)):
            start, end = i + 1, len(nums) - 1
            while start < end:
                res = nums[i] + nums[start] + nums[end]
                if res <= 0:
                    if not res:
                        answer.add((nums[i], nums[start], nums[end]))
                    start += 1
                else:
                    end -= 1

        return answer
