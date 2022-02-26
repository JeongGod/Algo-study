class Solution:
  def convert(self, s: str, numRows: int) -> str:
    order = []
    answer = []
    
    if numRows == 1:
      return s
    
    for i in range(numRows):
      answer.append([])
    for i in range(numRows):
      order.append(i)
    for i in range(numRows-2, 0, -1):
      order.append(i)
        
    for i,letter in enumerate(s):
      answer[order[i%len(order)]].append(letter)
        
    res = ''
    for a in answer:
      res += "".join(a)
        
    return res