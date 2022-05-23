class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        
        pointer = 0
        val = intervals[pointer]
        
        answer = []
        
        while pointer < len(intervals):
            if val[1] < intervals[pointer][0]:
                answer.append(val)
                val = intervals[pointer]
                continue
            val[1] = max(val[1], intervals[pointer][1])
            pointer += 1
        answer.append(val)
        return answer
