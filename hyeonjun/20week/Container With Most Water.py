class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        start, end = 0, len(height)-1

        while start < end:
            s_height, e_height = height[start], height[end]
            answer = max(answer,
                         (end-start) * min(s_height, e_height))  # length * width
            if s_height <= e_height:
                start += 1
            else:
                end -= 1

        return answer
