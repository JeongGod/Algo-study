class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row = len(matrix) 
        col = len(matrix[0])
        # 90도 회전 = x축 기준 뒤집기 + y = x 그래프 대칭이동 
        
        for i in range(row//2): # x축 기준 뒤집기
            for j in range(col):
                matrix[i][j], matrix[row-i-1][j] = matrix[row-i-1][j], matrix[i][j]
            
        for i in range(row): # y = x 그래프 대칭이동 
            for j in range(i,col):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        