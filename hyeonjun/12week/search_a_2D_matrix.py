class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(matrix: List[int], target: int) -> int:
            start = 0
            end = len(matrix) - 1
            mid = (start+end) // 2

            while start <= end:
                if matrix[mid] == target:
                    return mid
                elif matrix[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
                mid = (start+end)//2

            return mid

        first_column = [row[0] for row in matrix]
        cand_row = matrix[binary_search(first_column, target)]
        return True if target == cand_row[binary_search(cand_row, target)] else False
