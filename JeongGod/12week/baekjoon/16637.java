import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class B16637 {
    static long answer = (long) -1e9;
    static int[] nums;
    static char[] opers;
    public static int calc(int x, int y, char operation) {
        int result = 0;
        switch (operation) {
            case ('+'):
                result = x+y;
                break;
            case ('-'):
                result = x-y;
                break;
            case('*'):
                result = x*y;
                break;
        }

        return result;
    }

    public static void solve(int front, int back, int front_idx, int back_idx, boolean flag) {
        if (back_idx == nums.length ) {
            answer = Math.max(answer, calc(front, back, opers[front_idx]));
            return;
        }
        solve(calc(front, back, opers[front_idx]), nums[back_idx], back_idx-1, back_idx+1, false);
        if (!flag) solve(front, calc(back, nums[back_idx], opers[back_idx-1]), front_idx, back_idx+1, true);
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        System.out.println(answer);
        int n = Integer.parseInt(br.readLine());
        nums = new int[n/2 + 1];
        opers = new char[n/2];
        String form = br.readLine();

        for (int i=0; i<form.length(); i++) {
            if (i%2 == 0) nums[i/2] = form.charAt(i) - '0';
            else opers[i/2] = form.charAt(i);
        }
        if (form.length() == 1) {
            bw.write(String.valueOf(nums[0]));
            bw.flush();
            bw.close();
            return;
        }
        solve(nums[0], nums[1], 0, 2, false);
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}
