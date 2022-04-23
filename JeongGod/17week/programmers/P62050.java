package P62050;

import java.util.*;

class Point implements Comparable<Point>{
    int x, y, height;

    public Point(int x, int y, int height) {
        this.x = x;
        this.y = y;
        this.height = height;
    }

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return "Point{" +
                "x=" + x +
                ", y=" + y +
                ", height=" + height +
                '}';
    }

    @Override
    public int compareTo(Point o) {
        return this.height - o.height;
    }
}

class Solution {
    static boolean[][] visited;
    static int row, col;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int answer = 0;
    static PriorityQueue<Point> pq = new PriorityQueue<>();

    public boolean check(int x, int y) {
        return 0 <= x && x < row && 0 <= y && y < col;
    }

    public void makeIsland(int[][] land, int x, int y, int height) {
        ArrayDeque<Point> dq = new ArrayDeque<>();

        dq.add(new Point(x, y));
        visited[x][y] = true;

        while (!dq.isEmpty()) {
            Point point = dq.poll();
            int cx = point.x, cy = point.y;
            int curHeight = land[cx][cy];

            for (int i=0; i<4; i++) {
                int nx = cx + dx[i], ny = cy + dy[i];

                if (!check(nx, ny)) continue;
                if (visited[nx][ny]) continue;
                if (Math.abs(curHeight - land[nx][ny]) > height) {
                    pq.add(new Point(nx, ny, Math.abs(curHeight - land[nx][ny])));
                    continue;
                }

                visited[nx][ny] = true;
                dq.add(new Point(nx, ny));
            }
        }


    }

    public void connectBridge(int[][] land, int height) {
        Iterator iterator = pq.iterator();
        while(iterator.hasNext()) System.out.println(iterator.next());

        while (!pq.isEmpty()) {
            Point point = pq.poll();
            int cx = point.x, cy = point.y, ch = point.height;
            if (visited[cx][cy]) continue;

            System.out.println(cx + " " + cy + " " + ch);
            answer += ch;
            makeIsland(land, cx, cy, height);
        }
    }

    public int solution(int[][] land, int height) {
        /**
         1. 높이 차이가 h이하인 친구들을 BFS탐색으로 묶는다.
         2. 묶은 얘들끼리 사다리 연결을 한다.
         => 연결을 하면 같은 섬으로 취급한다.
         3.
         **/
        row = land.length;
        col = land[0].length;
        visited = new boolean[row][col];


        for (int x=0; x<row; x++) {
            for (int y=0; y<col; y++) {
                if (visited[x][y]) continue;
                makeIsland(land, x, y, height);
                connectBridge(land, height);
                for (int i=0; i<row; i++) System.out.println(Arrays.toString(visited[i]));
            }
        }


        return answer;
    }
}

public class P62050 {
    public static void main(String[] args) {
        System.out.println(new Solution().solution(new int[][] {{1, 4, 8, 10},{5, 5, 5, 5},{10, 10, 10, 10},{10, 10, 10, 20}}, 3));
        System.out.println(new Solution().solution(new int[][] {{10, 11, 10, 11}, {2, 21, 20, 10},{1, 20, 21, 11},{2, 1, 2, 1}}, 1));
    }
}
