class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        candirow = len(matrix) - 1
        for row in range(len(matrix)):
            if(matrix[row][0] > target):
                if(row == 0):
                    return False
                candirow = row - 1
                break
            elif(matrix[row][0] == target):
                return True
            
        for i in range(1, len(matrix[0])):
            if(matrix[candirow][i] == target):
                return True
            if(matrix[candirow][i] > target):
                return False
