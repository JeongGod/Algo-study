class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        if(len(height) == 1):
            return answer
        
        leftwall = height[0]
        rightwall = max(height[1:])
        
        for i in range(1, len(height)-1):
            if(height[i] < leftwall and height[i] < rightwall):
                if(leftwall < rightwall):
                    answer += leftwall - height[i]
                else:
                    answer += rightwall - height[i]
            else:
                leftwall = height[i]
                if(height[i] == rightwall):
                    rightwall = max(height[i+1:])
                    
        return answer