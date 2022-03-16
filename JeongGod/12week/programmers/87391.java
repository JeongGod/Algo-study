class Solution {
    static int rowStart, rowEnd, colStart, colEnd;
    public long solution(int n, int m, int x, int y, int[][] queries) {
        /**
        1. query를 역으로 도착지점부터 돌리면서 가능한 경우의 수를 파악한다.
            경우의 수는 직사각형 범위
        2. 가능한 직사각형이 격자내에 있는지 확인한다.
            1. 내부에 없다면 => 0
            2. 내부에 있다면
                직사각형의 내부만큼 가능한 경우의 수
                너비 * 높이
        **/
        rowStart = x; colStart = y; rowEnd = x; colEnd = y;
        
        for (int i = queries.length-1; i >= 0; i--) {
            int command = queries[i][0], dx = queries[i][1];
            switch (command) {
            // 반대로 간다.
            // 열 번호 증가
            case 0:
                // 만약 start가 벽이라면 커버가 가능하다.
                if (colStart != 0) {
                    colStart += dx;
                }
                colEnd += dx;
                if (colEnd > m-1) {    
                    colEnd = m-1;
                }
                break;
            // 열 번호 감소
            case 1:
                if (colEnd != m-1) {
                    colEnd -= dx;
                }
                colStart -= dx;
                if (colStart < 0) {
                    colStart = 0;
                }
                break;
            // 행 번호 증가
            case 2:
                if (rowStart != 0) {
                    rowStart += dx;
                }
                rowEnd += dx;
                if (rowEnd > n-1) {
                    rowEnd = n-1;
                }
                break;
            // 행 번호 감소
            case 3:
                if (rowEnd != n-1) {
                    rowEnd -= dx;
                }
                rowStart -= dx;
                if (rowStart < 0) {
                    rowStart = 0;
                }
                break;
            }
            // 불가능한 경우
            if (colStart > m-1 || colEnd < 0 || rowStart > n-1 || rowEnd < 0) {
                return 0L;
            }
        }
        // 직사각형의 넓이가 곧 가능한 경우의 수이다.
        return (long) (colEnd - colStart + 1) * (rowEnd - rowStart + 1);
    }
}