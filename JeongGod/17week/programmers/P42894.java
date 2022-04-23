package P42894;

import java.util.ArrayDeque;
import java.util.Arrays;

class Point {
    int x, y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return "Point{" +
                "x=" + x +
                ", y=" + y +
                '}';
    }
}

class Solution {
    static int R, C;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int answer = 0;

    public boolean check(int x, int y) {
        return 0 <= x && x < R && 0 <= y && y < C;
    }

    public Point[] searchBlocks(int[][] board, boolean[][] visited, int x, int y) {
        ArrayDeque<Point> dq = new ArrayDeque<>();

        dq.add(new Point(x, y));
        visited[x][y] = true;

        Point start = new Point(x, y);
        Point end = new Point(x, y);

        while (!dq.isEmpty()) {
            Point point = dq.poll();
            int cx = point.x, cy = point.y;

            for (int i=0; i<4; i++) {
                int nx = cx + dx[i], ny = cy + dy[i];

                if (!check(nx, ny) || board[nx][ny] != board[x][y]) continue;
                if (visited[nx][ny]) continue;

                if (start.x > nx) start.x = nx;
                if (start.y > ny) start.y = ny;
                if (end.x < nx) end.x = nx;
                if (end.y < ny) end.y = ny;

                visited[nx][ny] = true;
                dq.add(new Point(nx, ny));
            }
        }
        Point[] points = new Point[2];
        points[0] = start;
        points[1] = end;

        return points;
    }

    public boolean checkBlocks(int[][] board, Point[] points, int target) {


        for (int x = points[0].x; x <= points[1].x; x++) {
            for (int y = points[0].y; y <= points[1].y; y++) {
                if (board[x][y] != -1 && board[x][y] != target) return false;
            }
        }

        for (int x = points[0].x; x <= points[1].x; x++) {
            for (int y = points[0].y; y <= points[1].y; y++) {
                board[x][y] = 0;
            }
        }

        return true;
    }

    public void downBlocks(int[][] board, int sy, int ey) {

        for (int y=sy; y<=ey; y++) {
            for (int x=0; x<R; x++) {
                if (board[x][y] != -1 && board[x][y] != 0) break;
                board[x][y] = -1;
            }
        }
    }

    public boolean search(int[][] board) {
        boolean[][] visited = new boolean[R][C];

        for (int x=0; x<R; x++) {
            for (int y=0; y<C; y++) {
                if (board[x][y] == -1 || board[x][y] == 0 || visited[x][y]) continue;
                Point[] points = searchBlocks(board, visited, x, y);
                if (checkBlocks(board, points, board[x][y])) {
                    System.out.println(points[0] + " " + points[1]);
                    downBlocks(board, points[0].y, points[1].y);
                    answer += 1;
                    return true;
                }
            }
        }
        return false;
    }

    public int solution(int[][] board) {
        R = board.length;
        C = board[0].length;

        downBlocks(board, 0, C-1);



        while (true) {
            for (int[] i : board) System.out.println(Arrays.toString(i));
            if (!search(board)) break;
        }
        return answer;
    }
}



public class P42894 {
    public static void main(String[] args) {
    System.out.println(new Solution().solution(new int[][]{{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,4,0,0,0},{0,0,0,0,0,4,4,0,0,0},{0,0,0,0,3,0,4,0,0,0},{0,0,0,2,3,0,0,0,5,5},
    {1,2,2,2,3,3,0,0,0,5},{1,1,1,0,0,0,0,0,0,5}}));


    }
}

