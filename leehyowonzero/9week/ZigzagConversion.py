class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        
        answer = [[] for _ in range(numRows)]
        cycle = 2 * numRows - 2
        cycleidx = []
        for i in range(numRows):
            cycleidx.append(i)
        for i in range(numRows-2, 0, -1):
            cycleidx.append(i)
        
        for i, el in enumerate(s):
            answer[cycleidx[i%cycle]].append(el)
        
        ans = ''
        for i in range(numRows):
            ans += ''.join(answer[i])
            
        return ans