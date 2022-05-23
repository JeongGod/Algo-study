class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals.sort()

        ans.append([intervals[0][0]])
        target = intervals[0][1]
        for start, end in intervals[1:]:
            if target < start:
                ans[-1].append(target)
                ans.append([start])
                target = end
            else:
                target = max(target, end)

        ans[-1].append(target)

        return ans
