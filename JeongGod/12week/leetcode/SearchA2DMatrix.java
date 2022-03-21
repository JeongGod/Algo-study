import java.util.*;
class SearchA2DMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int i=0; i<matrix.length; i++) {
            // 가능한 열을 찾는다.
            if (matrix[i][0] <= target && target <= matrix[i][matrix[i].length-1]) {
                // target을 찾는다.

                return Arrays.binarySearch(matrix[i], target) >= 0;

            }
        }
        return false;
    }
}