class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        s, e = 0, len(height) - 1
        s_max, e_max = height[s], height[e]
        while s < e:
            s_max, e_max = max(height[s], s_max), max(height[e], e_max)

            if s_max <= e_max:
                answer += s_max - height[s]
                s += 1
            else:
                answer += e_max - height[e]
                e -= 1

        return answer
