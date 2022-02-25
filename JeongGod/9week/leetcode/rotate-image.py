class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        """
        n//2까지 돌린다.
        시작점은 0,0 ~ n//2-1, n//2-1까지
        끝점은 n-1, n-1 ~ n//2, n//2
        """
        e = n-1
        size = n
        for s in range(n//2):
            tmp = matrix[s][s:e+1]
            # 왼 -> 위
            for x in range(s, size):
                matrix[s][n-1-x] = matrix[x][s]

            # 아래 -> 왼
            for y in range(s, size):
                matrix[y][n-1-e] = matrix[e][y]
            
            # 오른 -> 아래
            for x in range(s+1, size):
                matrix[e][n-1-x] = matrix[x][e]
                
            # 임시 -> 오른
            for x in range(s, size):
                matrix[x][e] = tmp[x-s]

            e -= 1
            size -= 1
