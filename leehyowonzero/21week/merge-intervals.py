class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = [ ]
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if(intervals[i][0] <= end):
                end = max(end, intervals[i][1])
            else:
                answer.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        
        answer.append([start, end])
        return answer