import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class B2011 {
    private static int DIV = 1000000;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = br.readLine();
        if(input.charAt(0) == '0') {
            bw.write("0");
            bw.flush();
            return;
        }

        int[] dp = new int[input.length()+1];
        dp[0] = 1;
        dp[1] = 1;

        for (int i=2; i<input.length()+1; i++) {
            // 2번째는 1번째걸 본다.
            dp[i] = dp[i-1];
            // 이전 것과 현재 것을 합친 숫자
            int target = Integer.parseInt(input.substring(i-2, i));
            // 현재 값이 0이라면
            if (input.charAt(i-1) == '0') {
                // 이전에 있던게 1 또는 2여야만 한다.
                if (input.charAt(i-2) == '1' || input.charAt(i-2) == '2') {
                    dp[i] = dp[i-2];
                } else {
                    bw.write("0");
                    bw.flush();
                    return;
                }
            } else {
                if (input.charAt(i-2) == '0') {
                    continue;
                }
                if (target < 27) {
                    dp[i] += dp[i-2];
                }
            }

            dp[i] %= DIV;
        }

        bw.write(String.valueOf(dp[input.length()]));
        bw.flush();
    }
}
