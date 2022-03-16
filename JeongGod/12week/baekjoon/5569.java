import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class B5569 {
    static int MOD = 100000;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int W = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());

        int[][][] dp = new int[H][W][2];
        for (int i = 0; i < H; i++) {
            dp[i][0][0] = 1;
            dp[i][1][0] = 1;
            dp[i][1][1] = 1;
        }
        dp[0][1][0] = 0;
        for (int j = 0; j < W; j++) {
            dp[0][j][1] = 1;
            dp[1][j][0] = 1;
            dp[1][j][1] = 1;
        }
        dp[1][0][1] = 0;
        for (int i=2; i < H; i++) {
            for (int j=2; j<W; j++) {
                dp[i][j][1] = (dp[i][j-1][1] + dp[i-1][j-1][0])%MOD;
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j-1][1])%MOD;
            }
        }

        bw.write(String.valueOf((IntStream.of(dp[H-1][W-1]).sum())%MOD));
        bw.flush();
        bw.close();
    }
}
