class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        answer = 0
        while left < right:
            candi = (right - left) * min(height[left], height[right])
            answer = max(answer, candi)
            if(height[left] <= height[right]):
                nowheight = height[left]
                while nowheight >= height[left] and left < right:
                    left +=  1
                    
            else:
                nowheight = height[right]
                while nowheight >= height[right] and right > left:
                    right -=  1
        return answer