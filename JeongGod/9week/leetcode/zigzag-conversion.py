class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        board = [[] for _ in range(numRows)]
        
        target = len(s)
        row, add_row = 0, 1
        for idx in range(target):
            board[row].append(s[idx])
            row += add_row
            if not (0 < row < numRows - 1) :
                add_row *= -1
        
        result = ""
        for b in board:
            result += "".join(b)
        return result
