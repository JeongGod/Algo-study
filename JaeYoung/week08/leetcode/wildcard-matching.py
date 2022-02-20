from typing import List

 # 투 포인터를 최대로 이동

class Solution:

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        water = 0

        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[right]

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1

        return water
