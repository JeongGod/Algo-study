class Solution:
    def get_area(self, width, height):
        return width * height

    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            answer = max(answer, self.get_area(width, h))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return answer
