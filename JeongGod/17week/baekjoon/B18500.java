import java.io.*;
import java.util.*;

class Tuple {
    int x, y;

    public Tuple(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class B18500 {
    static char[][] board;
    static int r, c;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static boolean check(int x, int y) {
        return 0 <= x && x < r && 0 <= y && y < c;
    }


    public static boolean[][] checkMineral(int x, int y) {
        if (board[x][y] == '.') return null;
        Deque<Tuple> dq = new ArrayDeque<>();
        boolean[][] visited = new boolean[r][c];
        dq.add(new Tuple(x, y));
        visited[x][y] = true;
        // BFS탐색
        while (!dq.isEmpty()) {
            Tuple tuple = dq.poll();
            for (int i=0; i<4; i++) {
                int nx = tuple.x + dx[i], ny = tuple.y + dy[i];
                // 바닥에 붙어있다면
                if (nx == r) return null;
                // 범위 체크 및 방문 체크
                if (!check(nx, ny) || board[nx][ny] != 'x' || visited[nx][ny]) continue;
                Tuple newTuple = new Tuple(nx, ny);
                visited[nx][ny] = true;
                // 해당 미네랄 추가
                dq.add(newTuple);
            }
        }
        return visited;
    }
    public static void downMineral(boolean[][] visited) {
        while (true) {
            char[][] tmp = new char[r][c];
            for (int i=0; i<r; i++) {
                tmp[i] = board[i].clone();
            }
            // 가장 작은 높이를 찾았다면 그만큼 해당 클러스터를 내린다.
            for (int x=r-1; x>=0; x--) {
                for (int y=0; y<c; y++) {
                    // 클러스터를 내리자.
                    if (visited[x][y]) {
                        if (!check(x+1, y) || board[x+1][y] == 'x') {
                            board = tmp;
                            return;
                        }

                        board[x][y] = '.';
                        visited[x][y] = false;
                        board[x+1][y] = 'x';
                        visited[x+1][y] = true;
                    }
                }
            }
        }
    }

    public static void breakMineral(int x, int y) {
        // 미네랄을 부순다.
        board[x][y] = '.';


        // 한 방향씩 확인해본다.
        for (int i=1; i<5; i++) {
            if (!check(x+dx[i-1], y+dy[i-1])) continue;
            boolean[][] result = checkMineral(x+dx[i-1], y+dy[i-1]);


            // 부술 미네랄을 발견했다면
            if (result != null) {
                // 해당 미네랄을 내린다.
                downMineral(result);
                return;
            }

        }
    }

    public static void throwStick(int height, int go) {
        if (go == 0) {
            for (int y=0; y<c; y++) {
                // 던진 곳에서 미네랄을 발견한다면
                if (board[height][y] == 'x') {
                    breakMineral(height, y);
                    return;
                }
            }
        } else {
            for (int y=c-1; y>=0; y--) {
                if (board[height][y] == 'x') {
                    breakMineral(height, y);
                    return;
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        board = new char[r][c];

        for (int i=0; i<r; i++) {
            String t = br.readLine();
            for (int j=0; j<t.length(); j++) {
                board[i][j] = t.charAt(j);
            }
        }

        int n = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            int height = Integer.parseInt(st.nextToken());
            throwStick(r-height, i%2);
        }

        for (int i=0; i<r; i++) {
            System.out.println(String.valueOf(board[i]));
        }

    }
}