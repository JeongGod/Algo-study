import java.io.*;
import java.util.*;


public class B2342 {
    static int[][][] dp;
    static List<Integer> ddr;
    public static int calcCost(int cur, int target) {
        if (cur == target) return 1;
        else if (cur == 0) return 2;
        else if (cur % 2 == target % 2) return 4;
        else return 3;
    }

    public static int dfs(int left, int right, int depth) {
        if (depth == dp.length) return 0;
        if (dp[depth][left][right] != 0) return dp[depth][left][right];

        int leftFoot = dfs(ddr.get(depth), right, depth+1) + calcCost(left, ddr.get(depth));
        int rightFoot = dfs(left, ddr.get(depth), depth+1) + calcCost(right, ddr.get(depth));
        dp[depth][left][right] = Math.min(leftFoot, rightFoot);

        return dp[depth][left][right];
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        ddr = new ArrayList<>();
        while(true) {
            int val = Integer.parseInt(st.nextToken());
            if (val == 0) break;
            ddr.add(val);
        }
        if (ddr.size() == 0) {
            System.out.println(0);
            return;
        }
        dp = new int[ddr.size()][5][5];
        dp[0][0][0] = 0;
        System.out.println(dfs(0, 0, 0));

    }
}
